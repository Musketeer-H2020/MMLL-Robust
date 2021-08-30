# -*- coding: utf-8 -*-
'''
@author:  Marcos Fernandez Diaz
October 2020

Example of use: python pom3_Kmeans_master_local_flask.py --preprocessing <preprocessing> 

Parameters:
    - preprocessing: String indicating wether to apply standard normalization. Any string is valid.

'''


# Import general modules
import argparse
import time
import logging
import sys, os

# Add higher directory to python modules path.
sys.path.append("../../../../")

# To be imported from MMLL (pip installed)
from MMLL.comms.comms_local_Flask import Comms
from MMLL.nodes.MasterNode import MasterNode

# To be imported from demo_tools 
from demo_tools.data_connectors.Load_from_file import Load_From_File as DC
from demo_tools.mylogging.logger_v1 import Logger
from demo_tools.evaluation_tools import display, create_folders


# Set up logger
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--preprocessing', type=str, default=None, help='Type of preprocessing')

    FLAGS, unparsed = parser.parse_known_args()
    preprocessing = FLAGS.preprocessing

    # Set basic configuration
    dataset_name = 'pima'
    verbose = False
    pom = 3
    model_type = 'Kmeans'
    
    # Introduce manually the addresses for the workers
    workers_ids = ['0', '1']
    Nworkers = len(workers_ids)
    master_address = 'ma'


    # Create the directories for storing relevant outputs if they do not exist
    create_folders("./results/")

    # Setting up the logger
    logger = Logger('./results/logs/Master.log')

    # Task definition
    model_parameters = {}
    NC = 2
    Nmaxiter = 2
    tolerance = 0.001
    model_parameters.update({'Nmaxiter': Nmaxiter, 'NC': NC, 'tolerance': tolerance})

    # Creating the comms object
    display('===========================================', logger, verbose)
    display('Creating MasterNode under POM %d, communicating through local flask' %pom, logger, verbose)
    comms = Comms(workers_ids=workers_ids, my_id=master_address)

    # Creating MasterNode
    mn = MasterNode(pom, comms, logger, verbose)
    display('-------------------- Loading dataset %s --------------------------' %dataset_name, logger, verbose)

    # Load data
    # Warning: this data connector is only designed for the demos. In Musketeer, appropriate data connectors must be provided
    data_file = '../../../../input_data/' + dataset_name + '_demonstrator_data.pkl'
    try:
        dc = DC(data_file)
    except:
        display('Error - The file ' + dataset_name + '_demonstrator_data.pkl does not exist. Please download it from Box and put it under the following path: "' + os.path.abspath(os.path.join("","../../../../input_data/")) + '"', logger, verbose)
        sys.exit()

    # Normalization definition needed for preprocessing
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


    # Creating a ML model
    mn.create_model_Master(model_type, model_parameters=model_parameters)
    display('MMLL model %s is ready for training!' % model_type, logger, verbose)

    # Normalization of data in each worker before training
    if preprocessing is not None:
        mn.normalizer_fit_transform_workers(data_description, 'global_mean_std')

    # Start the training procedure.
    display('Training the model %s' % model_type, logger, verbose)
    t_ini = time.time()
    mn.fit()
    t_end = time.time()
    display('Training is complete: Training time = %s seconds' % str(t_end - t_ini)[0:6], logger, verbose)
    
    # Terminate workers
    display('Terminating all worker nodes.', logger, verbose)
    mn.terminate_workers()

    display('----------------------------------------------------------------------', logger, verbose)
    display('------------------------- END MMLL Procedure -------------------------', logger, verbose)
    display('----------------------------------------------------------------------\n', logger, verbose)
