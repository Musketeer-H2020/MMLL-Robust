# -*- coding: utf-8 -*-
'''
@author:  Marcos Fernandez Diaz
September 2020

Example of use: python pom2_NN_gradient_averaging_master_local_flask.py 

'''

# Import general modules
import time
import logging
import numpy as np
import sys, os

# Add higher directory to python modules path.
sys.path.append("../../../../")

# To be imported from MMLL (pip installed)
from MMLL.comms.comms_local_Flask import Comms
from MMLL.nodes.MasterNode import MasterNode

# To be imported from demo_tools 
from demo_tools.data_connectors.Load_from_file import Load_From_File as DC # Data connector
from demo_tools.mylogging.logger_v1 import Logger
from demo_tools.evaluation_tools import display


# Set up logger
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)



if __name__ == "__main__":
 
    dataset_name = 'mnist'
    verbose = False
    comms_type = 'local_flask'
    pom = 2
    model_type = 'NN'
    
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


    # Load the model architecture as defined by Keras model.to_json()
    try:
        with open('./keras_model_MLP_light_2.json', 'r') as json_file:
            model_architecture = json_file.read()
    except:
        display('Error - The file keras_model_MLP_light_2.json defining the neural network architecture is not available, please put it under the following path: "' + os.path.abspath(os.path.join("","./")) + '"', logger, verbose)
        sys.exit()

   
    # Task definition
    model_parameters = {}
    Nmaxiter = 2
    learning_rate = 0.0003
    optimizer = 'adam'
    loss = 'categorical_crossentropy'
    metric = 'accuracy'
    batch_size = 64
    num_epochs = 2
    model_averaging = 'False'
    model_parameters.update({'Nmaxiter': Nmaxiter, 'learning_rate': learning_rate, 'model_architecture': model_architecture,
                             'optimizer': optimizer, 'loss': loss, 'metric': metric, 'batch_size': batch_size, 'num_epochs': num_epochs, 
                             'model_averaging': model_averaging})

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


    # Creating a ML model
    mn.create_model_Master(model_type, model_parameters=model_parameters)
    display('MMLL model %s is ready for training!' % model_type, logger, verbose)


    # We start the training procedure.
    display('Training the model %s' % model_type, logger, verbose)
    t_ini = time.time()
    mn.fit()
    t_end = time.time()
    display('Training is complete: Training time = %s seconds' % str(t_end - t_ini)[0:6], logger, verbose)
    display('----------------------------------------------------------------------', logger, verbose)

    display('Terminating all worker nodes.', logger, verbose)
    mn.terminate_Workers()

    display('----------------------------------------------------------------------', logger, verbose)
    display('------------------------- END MMLL Procedure -------------------------', logger, verbose)
    display('----------------------------------------------------------------------\n', logger, verbose)
