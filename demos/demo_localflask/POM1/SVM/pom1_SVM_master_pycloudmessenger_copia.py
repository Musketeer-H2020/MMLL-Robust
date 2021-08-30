# -*- coding: utf-8 -*-
'''
@author:  Marcos Fernandez Diaz
November 2020

Example of use: python pom1_SVM_master_pycloudmessenger.py --user <user> --password <password> --task_name <task_name> --preprocessing <preprocessing>
    
Parameters:
    - user: String with the name of the user. If the user does not exist in the pycloudmessenger platform a new one will be created
    - password: String with the password
    - task_name: String with the name of the task. If the task already exists, an error will be displayed
    - normalization: String indicating whether to apply normalization. Possible options are std or minmax. By default no normalization is used.

'''

# Import general modules
import argparse
import logging
import json
import time
import sys, os
import numpy as np

# Add higher directory to python modules path.
sys.path.append("../../../../")

# To be imported from MMLL (pip installed)
from MMLL.nodes.MasterNode import MasterNode
from MMLL.comms.comms_local_Flask import Comms

# To be imported from demo_tools
from demo_tools.data_connectors.Load_from_file import Load_From_File as DC
from demo_tools.mylogging.logger_v1 import Logger
from demo_tools.evaluation_tools import display, plot_cm_seaborn, create_folders


# Set up logger
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)



if __name__ == "__main__":

    # Set basic configuration
    dataset_name = 'income_dv_small'
    verbose = False
    pom = 1
    model_type = 'SVM'
    normalization = 'no'

    # The master must know the workers ids
    workers_ids = ['0', '1']
    Nworkers = len(workers_ids)
    master_address = 'ma'


    # Create the directories for storing relevant outputs if they do not exist
    create_folders("./results/")

    # Setting up the logger 
    logger = Logger('./results/logs/Master.log')   

    # Task definition
    model_parameters = {}
    Nmaxiter = 4
    NC = 10
    tolerance = 0.001
    sigma = 0.1925
    C = 1
    NmaxiterGD = 100
    eta = 0.05
    model_parameters.update({'Nmaxiter': Nmaxiter, 'NC': NC, 'tolerance': tolerance, 'sigma': sigma, 'C': C, 'NmaxiterGD': NmaxiterGD, 'eta': eta})


    # Creating the comms object
    display('Creating MasterNode under POM %d, communicating through local flask' %pom, logger, verbose)
    comms = Comms(workers_ids=workers_ids, my_id=master_address)

    # Creating Masternode
    mn = MasterNode(pom, comms, logger, verbose)
    display('-------------------- Loading dataset %s --------------------------' %dataset_name, logger, verbose)

    # Load data
    # Warning: this data connector is only designed for the demos. In Musketeer, appropriate data
    # connectors must be provided
    data_file = '../../../../input_data/' + dataset_name + '_demonstrator_data.pkl'
    try:
        dc = DC(data_file)
    except:
        display('Error - The file ' + dataset_name + '_demonstrator_data.pkl does not exist. Please download it from Box and put it under the following path: "' + os.path.abspath(os.path.join("","../../../../input_data/")) + '"', logger, verbose)
        sys.exit()

    # Normalization definition needed for preprocessing
    input_data_description = None
    if dataset_name in ["income_dv_small"]:
        input_data_description = {
                            "NI": 107, 
                            "input_types": [{"type": "num"}] * 107
                            }

        target_data_description= {
        "NT": 1, 
        "output_types": [
        {"type": "bin", "name": "income", "definition": ">50K, <=50K"}
        ]
        }


    # Creating a ML model
    mn.create_model_Master(model_type, model_parameters=model_parameters)
    display('MMLL model %s is ready for training!' % model_type, logger, verbose)

    # Normalization of data in each worker before training
    if normalization=='std':
        normalizer = mn.normalizer_fit_transform_workers(input_data_description, 'global_mean_std')
    elif normalization=='minmax':
        normalizer = mn.normalizer_fit_transform_workers(input_data_description, 'global_min_max')

    # Start the training procedure.
    display('Training the model %s' % model_type, logger, verbose)
    t_ini = time.time()
    [Xval, yval] = dc.get_data_val()
    if normalization != 'no':
        Xval = normalizer.transform(Xval)
    # Update the labels for the algorithm to classify odd vs even digits
    print('yval before filter: ', yval[:25])
    print('Shape: ', yval.shape)
    val, count = np.unique(yval, return_counts=True)
    print('Unique values: ', val)
    print('counts: ', count)
    #yval = np.argmax(yval, axis=-1)
    filter_even = yval>0
    filter_odd = yval<=0
    yval[filter_even] = 1
    yval[filter_odd] = -1
    print('yval after filter: ', yval[:25])
    mn.fit(Xval=Xval, yval=yval)
    t_end = time.time()
    display('Training is complete: Training time = %s seconds' % str(t_end - t_ini)[0:6], logger, verbose)

   # Retrieving and saving the final model
    display('Retrieving the trained model from MasterNode', logger, verbose)
    model = mn.get_model()    
    # Warning: this save_model utility is only for demo purposes
    output_filename_model = './results/models/Master_' + dataset_name + '_model.pkl'
    mn.save_model(output_filename_model)

    # Making predictions on test data
    display('-------------  Obtaining predictions----------------------------------\n', logger, verbose)
    [Xtst, ytst] = dc.get_data_tst()
    if normalization != 'no':
        Xtst = normalizer.transform(Xtst)
    preds_tst = model.predict(Xtst)
    # Update the labels for the algorithm to classify odd vs even digits
    #ytst = np.argmax(ytst, axis=-1)
    val, count = np.unique(ytst, return_counts=True)
    print('ytst before filter: ', ytst[:25])
    print('Unique values: ', val)
    print('counts: ', count)
    filter_even = ytst>0
    filter_odd = ytst<=0
    ytst[filter_even] = 1
    ytst[filter_odd] = -1
    print('ytst after filter: ', ytst[:25])
    preds_tst = model.predict(Xtst)
    classes = [-1, 1]

    # Evaluating the results
    display('-------------  Evaluating --------------------------------------------\n', logger, verbose)
    # Warning, these evaluation methods are not part of the MMLL library, they are only intended
    # to be used for the demos. Use them at your own risk.
    output_filename = 'Master_SVM_confusion_matrix_' + dataset_name + '.png'
    title = 'SVM confusion matrix in test set master'
    plot_cm_seaborn(preds_tst, ytst, classes, title, output_filename, logger, verbose, normalize=True)

    # Terminate workers
    display('Terminating all worker nodes.', logger, verbose)
    mn.terminate_workers()

    display('----------------------------------------------------------------------', logger, verbose)
    display('------------------------- END MMLL Procedure -------------------------', logger, verbose)
    display('----------------------------------------------------------------------\n', logger, verbose)
