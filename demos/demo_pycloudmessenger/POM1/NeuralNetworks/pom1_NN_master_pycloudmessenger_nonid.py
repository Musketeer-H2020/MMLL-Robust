# -*- coding: utf-8 -*-
'''
@author:  Marcos Fernandez Diaz and Angel Navia Vñazquez
February 2020

Example of use: python pom1_NN_model_averaging_master_pycloudmessenger.py --user <user> --password <password> --task_name <task_name> --normalization <normalization>  --implementation <implementation>

Parameters:
    - user: String with the name of the user. If the user does not exist in the pycloudmessenger platform a new one will be created
    - password: String with the password
    - task_name: String with the name of the task. If the task already exists, an error will be displayed
    - normalization: String indicating whether to apply normalization. Possible options are std or minmax. By default no normalization is used
    - implementation: String indicating whether to use gradient_averaging or model_averaging implementation. By default the latter is used.
    - optimizer: String indicating the type of optimizer to use (only valid when gradient implementation=gradient_descent).

'''

# Import general modules
import argparse
import logging
import json
import time
import numpy as np
import sys, os
from distutils.util import strtobool
from sklearn.metrics import roc_curve, auc

# Add higher directory to python modules path.
sys.path.append("../../../../")
os.environ['KMP_WARNINGS'] = 'off' # Remove KMP_AFFINITY logs

# To be imported from MMLL (pip installed)
from MMLL.nodes.MasterNode import MasterNode
from MMLL.comms.comms_pycloudmessenger import Comms_master as Comms

# To be imported from demo_tools 
from demo_tools.task_manager_pycloudmessenger import Task_Manager
#from demo_tools.data_connectors.Load_from_file import Load_From_File as DC
from demo_tools.data_connectors.Load_from_file_nonid import Load_From_File_master as DC

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
    parser.add_argument('--user', type=str, default=None, help='User')
    parser.add_argument('--password', type=str, default=None, help='Password')
    parser.add_argument('--task_name', type=str, default=None, help='Name of the task')
    parser.add_argument('--normalization', type=str, default='no', choices=['no', 'std', 'minmax'], help='Type of normalization')
    parser.add_argument('--implementation', type=str, default='model_averaging', choices=['model_averaging', 'gradient_descent'], help='Type of implementation')
    parser.add_argument('--optimizer', type=str, default='SGD', choices=['SGD'], help='Gradient descent optimizer')
    parser.add_argument('--dataset', type=str, default=None, help='The dataset name')
    parser.add_argument('--Nworkers', type=str, default=None, help='The total number of workers')

    FLAGS, unparsed = parser.parse_known_args()
    user_name = FLAGS.user
    user_password = FLAGS.password
    task_name = FLAGS.task_name
    normalization = FLAGS.normalization
    implementation = FLAGS.implementation
    optimizer = FLAGS.optimizer
    dataset_name = FLAGS.dataset
    Nworkers = int(FLAGS.Nworkers)


    # Set basic configuration
    verbose = False
    pom = 1
    model_type = 'NN'

    Tfactor = 2

    if dataset_name == 'mnist_binclass':
        NI = 784
        NC = 5500
        if Nworkers == 4:
            Tmax =  Tfactor * 525.58
        if Nworkers == 8:
            Tmax =  Tfactor * 1016.5
        if Nworkers == 16:
            Tmax =  Tfactor * 2792.6
        if Nworkers == 32:
            Tmax =  Tfactor * 3627.1

    if dataset_name == 'ijcnn1':
        NI = 22
        NC = 2000
        if Nworkers == 4:
            Tmax =  Tfactor * 116.63
        if Nworkers == 8:
            Tmax =  Tfactor * 470.2
        if Nworkers == 16:
            Tmax =  Tfactor * 412.42
        if Nworkers == 32:
            Tmax =  Tfactor * 701.37

    if dataset_name == 'phishing':
        NI = 68
        NC = 1500
        if Nworkers == 4:
            Tmax =  Tfactor * 168.96
        if Nworkers == 8:
            Tmax =  Tfactor * 223.68
        if Nworkers == 16:
            Tmax =  Tfactor * 520.45
        if Nworkers == 32:
            Tmax =  Tfactor * 1120.1

    if dataset_name == 'income':
        NI = 107
        NC = 9000
        if Nworkers == 4:
            Tmax =  Tfactor * 1640.7
        if Nworkers == 8:
            Tmax =  Tfactor * 3359.6
        if Nworkers == 16:
            Tmax =  Tfactor * 5028.2
        if Nworkers == 32:
            Tmax =  Tfactor * 3742.7

    if dataset_name == 'webspam':
        NI = 254
        NC = 2000 
        if Nworkers == 4:
            Tmax =  Tfactor * 459.44
        if Nworkers == 8:
            Tmax =  Tfactor * 238.88
        if Nworkers == 16:
            Tmax =  Tfactor * 846.11
        if Nworkers == 32:
            Tmax =  Tfactor * 870.22

    # Create the directories for storing relevant outputs if they do not exist
    create_folders("./results/")

    # Setting up the logger 
    logger = Logger('./results/logs/Master_' + str(user_name) + '.log')   


    # Load the model architecture as defined by Keras model.to_json()
    keras_filename = 'keras_model_MLP_' + dataset_name + '.json'
    try:
        with open('./' + keras_filename, 'r') as json_file:
            model_architecture = json_file.read()
    except:
        display('Error - The file ' + keras_filename + ' defining the neural network architecture is not available, please put it under the following path: "' + os.path.abspath(os.path.join("","./")) + '"', logger, verbose)
        sys.exit()

    # Task definition
    if implementation.lower() == 'model_averaging':
        model_averaging = 'True'
    else:
        model_averaging = 'False'

    task_definition = {"quorum": Nworkers, 
                       "POM": pom, 
                       "model_type": model_type, 
                       "Nmaxiter": 500, 
                       "learning_rate": 0.15,
                       "model_architecture": model_architecture,
                       "optimizer": optimizer,
                       "momentum": 1,
                       "nesterov": 'False',
                       "loss": 'binary_crossentropy',
                       "metric": 'accuracy',
                       "batch_size": 4,
                       "num_epochs": 1,
                       "model_averaging": model_averaging
                      }


    # Load the credentials for pycloudmessenger
    display('===========================================', logger, verbose)
    display('Creating Master... ', logger, verbose)
    display('Please wait until Master is ready before launching the workers...', logger, verbose)
    # Note: this part creates the task and waits for the workers to join. This code is
    # intended to be used only at the demos, in Musketeer this part must be done in the client.
    credentials_filename = '../../musketeer.json'
    try:
        with open(credentials_filename, 'r') as f:
            credentials = json.load(f)
    except:
        display('Error - The file musketeer.json is not available, please put it under the following path: "' + os.path.abspath(os.path.join("","../../")) + '"', logger, verbose)
        sys.exit()

    # Create task and wait for participants to join
    tm = Task_Manager(credentials_filename)
    aggregator = tm.create_master_and_taskname(display, logger, task_definition, user_name=user_name, user_password=user_password, task_name=task_name)   
    display('Waiting for the workers to join task name = %s' % tm.task_name, logger, verbose)
    tm.wait_for_workers_to_join(display, logger)


    # Creating the comms object
    display('Creating MasterNode under POM %d, communicating through pycloudmessenger' %pom, logger, verbose)
    comms = Comms(aggregator)

    # Creating Masternode
    mn = MasterNode(pom, comms, logger, verbose)
    display('-------------------- Loading dataset %s --------------------------' %dataset_name, logger, verbose)

    # Load data
    # Warning: this data connector is only designed for the demos. In Musketeer, appropriate data
    # connectors must be provided
    data_path = '../../../../input_data/'
    try:
        dc = DC(data_path, dataset_name)
    except:
        display('Error - The file does not exist.' , logger, verbose)
        sys.exit()


    # Input and output data description needed for preprocessing
    number_inputs = NI
    feature_description = {"type": "num"}
    feature_array = [feature_description for index in range(number_inputs)]
    data_description = {
                        "NI": number_inputs, 
                        "input_types": feature_array
                        }

  
    # Creating a ML model
    model_parameters = {}
    model_parameters['learning_rate'] = float(task_definition['learning_rate'])
    model_parameters['Nmaxiter'] = int(task_definition['Nmaxiter'])
    model_parameters['model_architecture'] = task_definition['model_architecture']
    model_parameters['optimizer'] = task_definition['optimizer']
    model_parameters['momentum'] = task_definition['momentum']
    model_parameters['nesterov'] = task_definition['nesterov']
    model_parameters['loss'] = task_definition['loss']
    model_parameters['metric'] = task_definition['metric']
    model_parameters['batch_size'] = int(task_definition['batch_size'])
    model_parameters['num_epochs'] = int(task_definition['num_epochs'])
    model_parameters['model_averaging'] = task_definition['model_averaging']
    model_parameters.update({"Tmax": Tmax})

    mn.create_model_Master(model_type, model_parameters=model_parameters)

    display('#####################################################################', logger, verbose)
    display('MMLL model %s is ready for training!' % model_type, logger, verbose)
    display('MMLL model %s is waiting 2 minutes ... for the workers to be ready' % model_type, logger, verbose)
    display('#####################################################################', logger, verbose)

    # we wait 2 minutes for the workers to settle, this time does not count
    time.sleep(120)

    # Start the training procedure.
    display('Training the model %s' % model_type, logger, verbose)
    [Xval, yval] = dc.get_data_val()
    #yval = yval * 2 - 1
    t_ini = time.time()
    mn.fit(Xval=Xval, yval=yval)
    t_end = time.time()

   # Retrieving and saving the final model
    display('Retrieving the trained model from MasterNode', logger, verbose)
    model = mn.get_model()    
    # Warning: this save_model utility is only for demo purposes
    output_filename_model = './results/models/Master_' + str(user_name) + '_' + dataset_name + '_model.pkl'
    mn.save_model(output_filename_model)
    
    # Making predictions on test data
    display('-------------  Obtaining predictions----------------------------------\n', logger, verbose)
    [Xtst, ytst] = dc.get_data_tst()
    #ytst = ytst * 2 - 1
    preds_tst = model.predict(Xtst)

    fpr_tst, tpr_tst, thresholds_tst = roc_curve(list(ytst), preds_tst)
    roc_auc_tst = auc(fpr_tst, tpr_tst)

    '''
    # Making predictions on test data
    display('-------------  Obtaining predictions----------------------------------\n', logger, verbose)
    [Xtst, ytst] = dc.get_data_tst()
    if normalization != 'no':
        Xtst = normalizer.transform(Xtst)
    preds_tst = model.predict(Xtst)
    preds_tst = np.argmax(preds_tst, axis=-1) # Convert to labels
    y = np.argmax(ytst, axis=-1) # Convert to labels
    classes = np.arange(ytst.shape[1]) # 0 to 9
    '''

    display('\n##################################################################', logger, verbose)
    display('Dataset = %s, Nworkers=%d' % (dataset_name, Nworkers), logger, verbose)
    display('Training is complete: Training time = %s seconds' % str(t_end - t_ini).replace('.',',')[0:6], logger, verbose)
    display('AUC tst = %s' % str(roc_auc_tst).replace('.',','), logger, verbose)
    display('##################################################################\n', logger, verbose)

    # Terminate workers
    display('Terminating all worker nodes.', logger, verbose)
    mn.terminate_workers()

    display('----------------------------------------------------------------------', logger, verbose)
    display('------------------------- END MMLL Procedure -------------------------', logger, verbose)
    display('----------------------------------------------------------------------\n', logger, verbose)
