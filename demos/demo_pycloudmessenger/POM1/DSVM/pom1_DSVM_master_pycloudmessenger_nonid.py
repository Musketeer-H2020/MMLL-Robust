# -*- coding: utf-8 -*-
'''
@author:  Marcos Fernandez Diaz and Angel Navia
March 2021

Example of use: python pom1_DSVM_master_pycloudmessenger.py --user <user> --password <password> --task_name <task_name> --normalization <normalization> --dataset <dataset>
    
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
from sklearn.metrics import roc_curve, auc

# Add higher directory to python modules path.
sys.path.append("../../../../")

# To be imported from MMLL (pip installed)
from MMLL.nodes.MasterNode import MasterNode
from MMLL.comms.comms_pycloudmessenger import Comms_master as Comms

# To be imported from demo_tools
from demo_tools.task_manager_pycloudmessenger import Task_Manager
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
    parser.add_argument('--dataset', type=str, default=None, help='The dataset name')
    parser.add_argument('--Nworkers', type=str, default=None, help='The total number of workers')

    FLAGS, unparsed = parser.parse_known_args()
    user_name = FLAGS.user
    user_password = FLAGS.password
    task_name = FLAGS.task_name
    normalization = FLAGS.normalization
    dataset_name = FLAGS.dataset
    Nworkers = int(FLAGS.Nworkers)

    # Set basic configuration
    verbose = False
    pom = 1
    model_type = 'DSVM'

    if dataset_name == 'mnist_binclass':
        NI = 784
        NC = 5500
        sigma = 0.4 * np.sqrt(NI)
        Csvm = 800
        minvalue = 0.0
        maxvalue = 1.0

    if dataset_name == 'ijcnn1':
        NI = 22
        fsigma = 0.3
        sigma = fsigma * np.sqrt(NI)
        Csvm = 10
        NC = 2000
        minvalue = -1.0
        maxvalue = 1.0

    if dataset_name == 'phishing':
        NI = 68
        fsigma = 0.07
        sigma = fsigma * np.sqrt(NI)
        Csvm = 150
        NC = 1500
        minvalue = 0
        maxvalue = 0.3

    if dataset_name == 'income':
        NI = 107
        fsigma = 4
        sigma = fsigma * np.sqrt(NI)
        Csvm = 200
        minvalue = -4.0
        maxvalue = 14.0
        NC = 9000

    if dataset_name == 'webspam':
        NI = 254
        Csvm = 2000000
        minvalue = 0.0
        maxvalue = 1.0
        fsigma = 0.4
        sigma = fsigma * np.sqrt(NI)
        NC = 2000 


    # Create the directories for storing relevant outputs if they do not exist
    create_folders("./results/")

    # Setting up the logger 
    logger = Logger('./results/logs/Master_' + str(user_name) + '.log')   

    # Task definition
    task_definition = {"quorum": Nworkers, 
                       "POM": pom, 
                       "model_type": model_type, 
                       "NC": NC, 
                       "Nmaxiter": 5, 
                       "tolerance": 0.05,
                       "sigma": sigma,
                       "C": Csvm,
                       "eps": 0.0000001
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
    display('Creating MasterNode under POM%d, communicating through pycloudmessenger' %pom, logger, verbose)
    comms = Comms(aggregator)

    # Creating Masternode
    mn = MasterNode(pom, comms, logger, verbose)
    display('-------------------- Loading dataset %s --------------------------' % dataset_name, logger, verbose)

    # Load data
    # Warning: this data connector is only designed for the demos. In Musketeer, appropriate data
    # connectors must be provided
    data_path = '../../../../input_data/'
    try:
        dc = DC(data_path, dataset_name)
    except:
        display('Error - The file does not exist.' , logger, verbose)
        sys.exit()

    # Normalization definition needed for preprocessing
    number_inputs = NI
    feature_description = {"type": "num"}
    feature_array = [feature_description for index in range(number_inputs)]
    data_description = {
                        "NI": number_inputs, 
                        "input_types": feature_array
                        }


    # Creating a ML model
    model_parameters = {}
    model_parameters['NC'] = int(task_definition['NC'])
    model_parameters['Nmaxiter'] = int(task_definition['Nmaxiter'])
    model_parameters['tolerance'] = float(task_definition['tolerance'])
    model_parameters['sigma'] = float(task_definition['sigma'])
    model_parameters['C'] = float(task_definition['C'])
    model_parameters['eps'] = float(task_definition['eps'])
    model_parameters['NI'] = NI
    model_parameters['minvalue'] = minvalue
    model_parameters['maxvalue'] = maxvalue

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
    yval = yval * 2 - 1
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
    ytst = ytst * 2 - 1
    preds_tst = model.predict(Xtst)
    fpr_tst, tpr_tst, thresholds_tst = roc_curve(list(ytst), preds_tst)
    roc_auc_tst = auc(fpr_tst, tpr_tst)

    # Terminate workers
    display('Terminating all worker nodes.', logger, verbose)
    mn.terminate_workers()

    display('----------------------------------------------------------------------', logger, verbose)
    display('------------------------- END MMLL Procedure -------------------------', logger, verbose)
    display('----------------------------------------------------------------------\n', logger, verbose)

    display('\n##################################################################', logger, verbose)
    display('Dataset = %s, Nworkers=%d' % (dataset_name, Nworkers), logger, verbose)
    display('Training is complete: Training time = %s seconds' % str(t_end - t_ini).replace('.',',')[0:6], logger, verbose)
    display('AUC tst = %s' % str(roc_auc_tst).replace('.',','), logger, verbose)
    display('##################################################################\n', logger, verbose)

