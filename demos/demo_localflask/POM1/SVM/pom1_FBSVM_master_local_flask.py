# -*- coding: utf-8 -*-
'''
@author:  Marcos Fernandez Diaz
May 2020

Example of use: python pom1_Kmeans_master_local_flask.py --dataset <dataset> --num_workers <num_workers>

'''

# Import general modules
import argparse
import time
import numpy as np
import logging
import sys, os

# Add higher directory to python modules path.
sys.path.append("../../../../")

# To be imported from MMLL (pip installed)
from MMLL.comms.comms_local_Flask import Comms
from MMLL.nodes.MasterNode import MasterNode

# To be imported from demo_tools 
from demo_tools.data_connectors.Load_from_file import Load_From_File as DC # Data connector
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
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, default=None, help='The dataset to be used')
    parser.add_argument('--num_workers', type=int, default=2, choices=[1, 2, 3, 4, 5], help='The dataset to be used')

    FLAGS, unparsed = parser.parse_known_args()
    dataset_name = FLAGS.dataset
    num_workers = FLAGS.num_workers

    # Set basic configuration
    verbose = False
    pom = 1
    model_type = 'SVM'
    
    # The master must know the workers ids
    workers_ids = [str(worker) for worker in range(num_workers)]
    Nworkers = len(workers_ids)
    master_address = 'ma'


    # Create the directories for storing relevant outputs if they do not exist
    create_folders("./results/")

    # Logging is optional, if you do not want to log messages, simply set logger=None
    logger = Logger('./results/logs/Master.log')


    # Task definition
    model_parameters = {}
    Nmaxiter = 2
    NC = 500
    tolerance = 0.1
    sigma = 0.4 * np.sqrt(784)
    C = 800
    num_epochs_worker = 10
    mu = 0.5
    eps = 0.0000001
    NI = 784
    minvalue = 0
    maxvalue = 1
    model_parameters.update({'Nmaxiter': Nmaxiter, 'NC': NC, 'tolerance': tolerance, 'sigma': sigma, 'C': C, 'num_epochs_worker': num_epochs_worker, 'mu': mu, 'eps': eps, 'NI': NI, 'minvalue': minvalue, 'maxvalue': maxvalue})


    # Creating the comms object
    display('Creating MasterNode under POM %d, communicating through local flask' %pom, logger, verbose)
    comms = Comms(workers_ids=workers_ids, my_id=master_address)


    # Creating MasterNode
    mn = MasterNode(pom, comms, logger, verbose)
    display('-------------------- Loading dataset %s --------------------------' %dataset_name, logger, verbose)
    # Warning: this data connector is only designed for the demos. In Musketeer, appropriate data
    # connectors must be provided
    data_file = '../../../../input_data/' + dataset_name + '_demonstrator_data.pkl'
    try:
        dc = DC(data_file)
    except:
        display('Error - The file ' + dataset_name + '_demonstrator_data.pkl does not exist. Please download it from Box and put it under the following path: "' + os.path.abspath(os.path.join("","../../../../input_data/")) + '"', logger, verbose)
        sys.exit()

    # Get the validation data
    [Xval, yval] = dc.get_data_val()
    # Update the labels for the algorithm to classify odd vs even digits
    yval = np.argmax(yval, axis=-1)
    filter_even = yval%2 == 0
    filter_odd = yval%2 != 0
    yval[filter_even] = 1
    yval[filter_odd] = -1
    mn.set_validation_data(dataset_name, Xval, yval)
    display('MasterNode loaded %d patterns for validation' % mn.NPval, logger, verbose)


    # Creating a ML model
    mn.create_model_Master(model_type, model_parameters=model_parameters)
    display('MMLL model %s is ready for training!' % model_type, logger, verbose)


    # We start the training procedure.
    display('Training the model %s' % model_type, logger, verbose)
    t_ini = time.time()
    mn.fit(Xval, yval)
    t_end = time.time()
    display('Training is complete: Training time = %s seconds' % str(t_end - t_ini)[0:6], logger, verbose)
    display('----------------------------------------------------------------------', logger, verbose)

    display('Retrieving the trained model from MasterNode', logger, verbose)
    model = mn.get_model()

    
    # Warning: this save_model utility is only for demo purposes
    output_filename_model = './results/models/Master_' + dataset_name + '_model.pkl'
    mn.save_model(output_filename_model)

    display('-------------  Obtaining predictions----------------------------------\n', logger, verbose)
    [Xtst, ytst] = dc.get_data_tst()
    # Update the labels for the algorithm to classify odd vs even digits
    ytst = np.argmax(ytst, axis=-1)
    filter_even = ytst%2 == 0
    filter_odd = ytst%2 != 0
    ytst[filter_even] = 1
    ytst[filter_odd] = -1
    preds_tst = model.predict(Xtst)
    filter_neg = preds_tst < 0
    filter_pos = preds_tst >= 0
    preds_tst[filter_pos] = 1
    preds_tst[filter_neg] = -1
    classes = [-1, 1]

    display('-------------  Evaluating --------------------------------------------\n', logger, verbose)
    # Warning, these evaluation methods are not part of the MMLL library, they are only intended
    output_filename = 'Master_confusion_matrix_' + dataset_name + '.png'
    title = 'SVM confusion matrix in test set master'
    plot_cm_seaborn(preds_tst, ytst, classes, title, output_filename, logger, verbose, normalize=True)

    display('Terminating all worker nodes.', logger, verbose)
    mn.terminate_workers()

    display('----------------------------------------------------------------------', logger, verbose)
    display('------------------------- END MMLL Procedure -------------------------', logger, verbose)
    display('----------------------------------------------------------------------\n', logger, verbose)
