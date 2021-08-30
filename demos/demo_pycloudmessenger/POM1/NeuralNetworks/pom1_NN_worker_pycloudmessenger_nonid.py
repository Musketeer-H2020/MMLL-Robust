# -*- coding: utf-8 -*-
'''
@author:  Marcos Fernandez Diaz and Angel Navia Vázquez
November 2020

Example of use: python pom1_NN_worker_pycloudmessenger.py --user <user> --password <password> --task_name <task_name> --id <id>

Parameters:
    - user: String with the name of the user. If the user does not exist in the pycloudmessenger platform a new one will be created
    - password: String with the password
    - task_name: String with the name of the task. If the task already exists, an error will be displayed
    - id: Integer representing the partition of data to be used by the worker. Each worker should use a different partition, possible values are 0 to 4.

'''

# Import general modules
import argparse
import logging
import json
import numpy as np
import sys, os

# Add higher directory to python modules path.
sys.path.append("../../../../")

# To be imported from MMLL (pip installed)
from MMLL.nodes.WorkerNode import WorkerNode
from MMLL.comms.comms_pycloudmessenger import Comms_worker as Comms

# To be imported from demo_tools
from demo_tools.task_manager_pycloudmessenger import Task_Manager
#from demo_tools.data_connectors.Load_from_file import Load_From_File as DC
from demo_tools.data_connectors.Load_from_file_nonid import Load_From_File_worker as DC

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
    parser.add_argument('--id', type=int, default=None, help='The address of the worker')
    parser.add_argument('--dataset', type=str, default=None, help='The dataset name')
    parser.add_argument('--Nworkers', type=str, default=None, help='The total number of workers')

    FLAGS, unparsed = parser.parse_known_args()
    user_name = FLAGS.user
    user_password = FLAGS.password
    task_name = FLAGS.task_name
    data_partition_id = FLAGS.id # This integer identifies the data partition used for the worker
    dataset_name = FLAGS.dataset
    Nworkers = int(FLAGS.Nworkers)

    # Set basic configuration
    verbose = False
    pom = 1
    model_type = 'NN'


    # Create the directories for storing relevant outputs if they do not exist
    create_folders("./results/")

    # Setting up the logger
    logger = Logger('./results/logs/Worker_' + str(user_name) + '.log')


    # Load the credentials for pycloudmessenger
    display('===========================================', logger, verbose)
    display('Creating Worker...', logger, verbose)
    # Note: this part creates the worker (participant) and it joins the task. This code is
    # intended to be used only at the demos, in Musketeer this part must be done in the client. 
    credentials_filename = '../../musketeer.json'
    try:
        with open(credentials_filename, 'r') as f:
            credentials = json.load(f)
    except:
        display('Error - The file musketeer.json is not available, please put it under the following path: "' + os.path.abspath(os.path.join("","../../")) + '"', logger, verbose)
        sys.exit()

    # Create user and join task
    tm = Task_Manager(credentials_filename)
    participant = tm.create_worker_and_join_task(user_name, user_password, task_name, display, logger)
    display("Worker %s has joined task %s" %(user_name, task_name), logger, verbose)

    # Creating the comms object
    display('Creating WorkerNode under POM %d, communicating through pycloudmessenger' %pom, logger, verbose)
    comms = Comms(participant, user_name)
    
    # Creating Workernode
    wn = WorkerNode(pom, comms, logger, verbose)
    display('-------------------- Loading dataset %s --------------------------' % dataset_name, logger, verbose)

    # Load data
    # Warning: this data connector is only designed for the demos. In Musketeer, appropriate data
    # connectors must be provided
    data_path = '../../../../input_data/'
    try:
        dc = DC(data_path, dataset_name, Nworkers, data_partition_id)
    except:
        display('Error - The file does not exist.', logger, verbose)
        sys.exit()

    # Get train/test data and set training data
    [Xtr, ytr] = dc.get_data_train_Worker(int(data_partition_id))
    # Update the labels for the algorithm to classify odd vs even digits
    #ytr = ytr * 2 - 1
    wn.set_training_data(dataset_name, Xtr, ytr)
    display('WorkerNode loaded %d patterns for training' % wn.NPtr, logger, verbose)

    # Creating a ML model and start training procedure
    wn.create_model_worker(model_type)
    display('MMLL model %s is ready for training!' %model_type, logger, verbose)
    display('Worker_' + model_type + ' %s is running...' %user_name, logger, verbose)
    wn.run()
    display('Worker_' + model_type + ' %s: EXIT' %user_name, logger, verbose)


