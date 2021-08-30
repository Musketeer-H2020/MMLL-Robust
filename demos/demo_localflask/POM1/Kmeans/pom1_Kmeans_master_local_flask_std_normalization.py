# -*- coding: utf-8 -*-
'''
@author:  Marcos Fernandez Diaz
May 2020

Example of use: pom1_Kmeans_master_local_flask_std_normalization.py

'''

# Import general modules
import argparse
import logging
import json
import time
import sys, os

# Add higher directory to python modules path.
sys.path.append("../../../../")

# To be imported from MMLL (pip installed)
from MMLL.nodes.MasterNode import MasterNode
from MMLL.comms.comms_local_Flask import Comms

# To be imported from demo_tools
from demo_tools.data_connectors.Load_from_file import Load_From_File as DC                          # Data connector
from demo_tools.mylogging.logger_v1 import Logger
from demo_tools.evaluation_tools import display, Kmeans_plot


# Set up logger
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)



if __name__ == "__main__":
    
    dataset_name = 'pima'
    verbose = False
    comms_type = 'pycloudmessenger'
    pom = 1
    model_type = 'Kmeans'

    # The master must know the workers ids
    workers_ids = ['0', '1']
    Nworkers = len(workers_ids)
    master_address = 'ma'

    
    # Create the directories for storing relevant outputs if they do not exist
    if not os.path.exists("../results/logs/"):
        os.makedirs("../results/logs/") # Create directory for the logs
    if not os.path.exists("../results/figures/"):
        os.makedirs("../results/figures/") # Create directory for the figures
    if not os.path.exists("../results/models/"):
        os.makedirs("../results/models/") # Create directory for the models


    # Setting up the logger
    logger = Logger('../results/logs/Local_flask_Master.log')


    # Task definition
    model_parameters = {}
    Nmaxiter = 2
    NC = 2
    tolerance = 0.001
    # Data description
    data_description = {
                        "NI": 8, 
                        "input_types": [
                        {"type": "num"},
                        {"type": "num"},
                        {"type": "num"},
                        {"type": "num"},
                        {"type": "num"},
                        {"type": "num"},
                        {"type": "num"},
                        {"type": "num"}
                        ]
                        }
    model_parameters.update({'Nmaxiter': Nmaxiter, 'NC': NC, 'tolerance': tolerance, 'data_description': data_description})


    # Creating the comms object
    display('Creating MasterNode under POM %d, communicating through local flask' %pom, logger, verbose)
    comms = Comms(workers_ids=workers_ids, my_id=master_address)


    # Creating Masternode
    mn = MasterNode(pom, comms, logger, verbose)
    display('-------------------- Loading dataset %s --------------------------' % dataset_name, logger, verbose)
    # Warning: this data connector is only designed for the demos. In Musketeer, appropriate data connectors must be provided


    data_file = '../../../../input_data/' + dataset_name + '_demonstrator_data.pkl'
    try:
        dc = DC(data_file)
    except:
        display('Error - The file ' + dataset_name + '_demonstrator_data.pkl does not exist. Please download it from Box and put it under the following path: "' + os.path.abspath(os.path.join("","../../../../input_data/")) + '"', logger, verbose)
        sys.exit()

  
    #---------------  Creating a ML model (Master side) ---------------------  
    mn.create_model_Master(model_type, model_parameters=model_parameters)
    display('MMLL model %s is ready for training!' % model_type, logger, verbose)


    ##############################################################################
    ######## Data normalization prior to training ################################
    ##############################################################################
    # We normalize the data before training
    # normalizes workers data and returns the normalizer object
    normalizer = mn.normalizer_fit_transform_workers(data_description, 'global_mean_std')
        

    # We start the training procedure.
    display('Training the model %s' % model_type, logger, verbose)
    t_ini = time.time()
    mn.fit()
    t_end = time.time()
    display('Training is complete: Training time = %s seconds' % str(t_end - t_ini)[0:6], logger, verbose)
    display('----------------------------------------------------------------------', logger, verbose)

    display('Retrieving the trained model from MasterNode', logger, verbose)
    model = mn.get_model()
    
    # Warning: this save_model utility is only for demo purposes
    output_filename_model = '../results/models/POM' + str(pom) + '_' + model_type + '_master_' + dataset_name + '_model.pkl'
    mn.save_model(output_filename_model)

    display('-------------  Obtaining predictions----------------------------------\n', logger, verbose)
    [Xtst, ytst] = dc.get_data_tst()
    Xtst = normalizer.transform(Xtst)
    preds_tst = model.predict(Xtst)

    display('-------------  Evaluating --------------------------------------------\n', logger, verbose)
    # Warning, these evaluation methods are not part of the MMLL library, they are only intended
    # to be used for the demos. Use them at your own risk.
    Kmeans_plot(Xtst, preds_tst, 'Kmeans clustering with 2 PCA components in test set', model_type, dataset_name, logger, verbose)

    display('Terminating all worker nodes.', logger, verbose)
    mn.terminate_Workers()

    display('----------------------------------------------------------------------', logger, verbose)
    display('------------------------- END MMLL Procedure -------------------------', logger, verbose)
    display('----------------------------------------------------------------------\n', logger, verbose)
