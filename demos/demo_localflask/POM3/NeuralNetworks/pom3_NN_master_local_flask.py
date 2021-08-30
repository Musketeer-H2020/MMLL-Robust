# -*- coding: utf-8 -*-
'''
@author:  Marcos Fernandez Diaz
November 2020

Example of use: python pom3_NN_master_local_flask.py --preprocessing <preprocessing> --implementation <implementation>

Parameters:
    - preprocessing: String indicating whether to apply standard normalization. Any string is valid. By default no normalization is used.
    - implementation: String indicating whether to use gradient_averaging or model_averaging implementation. By default the latter is used. 

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
    parser.add_argument('--implementation', type=str, default='model_averaging', help='Type of preprocessing')

    FLAGS, unparsed = parser.parse_known_args()
    preprocessing = FLAGS.preprocessing
    implementation = FLAGS.implementation

    # Set basic configuration
    dataset_name = 'mnist'
    verbose = False
    pom = 3
    model_type = 'NN'
    
    # The master must know the workers ids
    workers_ids = ['0', '1']
    Nworkers = len(workers_ids)
    master_address = 'ma'


    # Create the directories for storing relevant outputs if they do not exist
    create_folders("./results/")

    # Setting up the logger
    logger = Logger('./results/logs/Master.log')


    # Load the model architecture in the format defined by Keras model.to_json()
    keras_filename = 'keras_model_MLP_light_2.json'
    try:
        with open('./' + keras_filename, 'r') as json_file:
            model_architecture = json_file.read()
    except:
        display('Error - The file ' + keras_filename + ' defining the neural network architecture is not available, please put it under the following path: "' + os.path.abspath(os.path.join("","./")) + '"', logger, verbose)
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
    if implementation.lower() == 'model_averaging':
        model_averaging = 'True'
    elif implementation.lower() == 'gradient_averaging':
        model_averaging = 'False'
    else:
        display('Error - Unknown implementation. Select either model_averaging or gradient_averaging.', logger, verbose)
        sys.exit()
    model_parameters.update({'Nmaxiter': Nmaxiter, 'learning_rate': learning_rate, 'model_architecture': model_architecture,
                             'optimizer': optimizer, 'loss': loss, 'metric': metric, 'batch_size': batch_size, 'num_epochs': num_epochs, 
                             'model_averaging': model_averaging})

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
    number_inputs = 784
    feature_description = {"type": "num"}
    feature_array = [feature_description for index in range(number_inputs)]
    data_description = {
                        "NI": number_inputs, 
                        "input_types": feature_array
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
