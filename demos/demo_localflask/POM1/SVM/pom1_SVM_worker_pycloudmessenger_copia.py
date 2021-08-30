# -*- coding: utf-8 -*-
'''
@author:  Marcos Fernandez Diaz
November 2020

Example of use: python pom1_SVM_worker_pycloudmessenger.py --user <user> --password <password> --task_name <task_name> --id <id>

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
import sys, os
import numpy as np

# Add higher directory to python modules path.
sys.path.append("../../../../")

# To be imported from MMLL (pip installed)
from MMLL.nodes.WorkerNode import WorkerNode
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
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', type=int, default=None, choices=[0, 1, 2, 3, 4], help='The data partition of the worker')

    FLAGS, unparsed = parser.parse_known_args()
    data_partition_id = FLAGS.id # This integer identifies the data partition used for the worker

    # Set basic configuration
    dataset_name = 'income_dv_small'
    verbose = False
    pom = 1
    model_type = 'SVM'


    # Create the directories for storing relevant outputs if they do not exist
    create_folders("./results/")

    # Setting up the logger
    logger = Logger('./results/logs/Worker_' + str(data_partition_id) + '.log')


    # Load the credentials for pycloudmessenger
    display('===========================================', logger, verbose)
    display('Creating Worker...', logger, verbose)
    # ==================================================
    # Note: this part creates the worker (participant) and it joins the task. This code is
    # intended to be used only at the demos, in Musketeer this part must be done in the client. 
    # ==================================================


    # Creating the comms object
    display('Creating WorkerNode under POM %d, communicating through pycloudmessenger' %pom, logger, verbose)
    comms = Comms(my_id=data_partition_id)
    
    # Creating Workernode
    wn = WorkerNode(pom, comms, logger, verbose)
    display('-------------------- Loading dataset %s --------------------------' % dataset_name, logger, verbose)

    # Load data
    # Warning: this data connector is only designed for the demos. In Musketeer, appropriate data
    # connectors must be provided
    data_file = '../../../../input_data/' + dataset_name + '_demonstrator_data.pkl'
    try:
        dc = DC(data_file)
    except:
        display('Error - The file ' + dataset_name + '_demonstrator_data.pkl does not exist. Please download it from Box and put it under the following path: "' + os.path.abspath(os.path.join("","../../../../input_data/")) + '"', logger, verbose)
        sys.exit()

    # Get train/test data and set training data
    [Xtr, ytr, _, _, Xtst, ytst] = dc.get_all_data_Worker(int(data_partition_id))
    # Update the labels for the algorithm to classify odd vs even digits
    #ytr = np.argmax(ytr, axis=-1)
    filter_even = ytr>0
    filter_odd = ytr<=0
    ytr[filter_even] = 1
    ytr[filter_odd] = -1
    wn.set_training_data(dataset_name, Xtr, ytr)
    display('WorkerNode loaded %d patterns for training' % wn.NPtr, logger, verbose)

    # Creating a ML model and start training procedure 
    wn.create_model_worker(model_type)
    display('MMLL model %s is ready for training!' %model_type, logger, verbose)
    display('Worker_' + model_type + ' %s is running...' %data_partition_id, logger, verbose)
    wn.run()
    display('Worker_' + model_type + ' %s: EXIT' %data_partition_id, logger, verbose)

    # Retrieving and saving the trained model
    display('Retrieving the trained model from WorkerNode', logger, verbose)
    model = wn.get_model()    
    # Warning: this save_model utility is only for demo purposes
    output_filename_model = './results/models/Worker_' + str(data_partition_id) + '_' + dataset_name + '_model.pkl'
    wn.save_model(output_filename_model)

    # Making predictions on test data
    display('-------------  Obtaining predictions------------------------------------\n', logger, verbose)
    preprocessors = wn.get_preprocessors()
    if preprocessors is not None:
        for prep_model in preprocessors: # Apply stored preprocessor sequentially (in the same order received)
            Xtst = prep_model.transform(Xtst)
            display('Test data transformed using %s' %prep_model.name, logger, verbose)
    # Update the labels for the algorithm to classify odd vs even digits
    #ytst = np.argmax(ytst, axis=-1)
    filter_even = ytst>0
    filter_odd = ytst<=0
    ytst[filter_even] = 1
    ytst[filter_odd] = -1
    preds_tst = model.predict(Xtst)
    classes = [-1, 1]

    # Evaluating the results
    display('-------------  Evaluating --------------------------------------------\n', logger, verbose)
    # Warning, these evaluation methods are not part of the MMLL library, they are only intended
    # to be used for the demos. Use them at your own risk.
    output_filename = 'Worker_' + str(data_partition_id) + '_SVM_confusion_matrix_' + dataset_name + '.png'
    title = 'SVM confusion matrix in test set worker'
    plot_cm_seaborn(preds_tst, ytst, classes, title, output_filename, logger, verbose, normalize=True)

