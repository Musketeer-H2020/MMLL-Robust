# -*- coding: utf-8 -*-
'''
@author:  Marcos Fernandez Diaz
May 2020

Example of use: python pom1_Kmeans_worker_local_flask.py --id 0

Parameters:
    - id: Integer representing the partition of data to be used by the worker. Each worker should use a different partition, possible values are 0 to 4.

'''

# Import general modules
import argparse
import numpy as np
import logging
import sys, os

# Add higher directory to python modules path.
sys.path.append("../../../../")

# To be imported from MMLL (pip installed)
from MMLL.comms.comms_local_Flask import Comms
from MMLL.nodes.WorkerNode import WorkerNode

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
    parser.add_argument('--id', type=int, default=None, choices=[0, 1, 2, 3, 4], help='The address of the worker')
    parser.add_argument('--dataset', type=str, default=None, help='The dataset to be used')

    FLAGS, unparsed = parser.parse_known_args()
    worker_address = FLAGS.id
    dataset_name = FLAGS.dataset

    # Set basic configuration
    verbose = False
    pom = 1
    model_type = 'SVM'


    # Create the directories for storing relevant outputs if they do not exist
    create_folders("./results/")

    # Setting up the logger
    logger = Logger('./results/logs/Worker_' + str(worker_address) + '.log')


    display('===========================================', logger, verbose)
    display('Creating Worker...', logger, verbose)
    # Creating the comms object
    display('Creating WorkerNode under POM %d, communicating through local flask' %pom, logger, verbose)
    comms = Comms(my_id=worker_address)


    # Creating Workernode
    wn = WorkerNode(pom, comms, logger, verbose)
    display('-------------------- Loading dataset %s --------------------------' % dataset_name, logger, verbose)

    # Warning: this data connector is only designed for the demos. In Musketeer, appropriate data
    # connectors must be provided
    data_file = '../../../../input_data/' + dataset_name + '_demonstrator_data.pkl'
    try:
        dc = DC(data_file)
    except:
        display('Error - The file ' + dataset_name + '_demonstrator_data.pkl does not exist. Please download it from Box and put it under the following path: "' + os.path.abspath(os.path.join("","../../../../input_data/")) + '"', logger, verbose)
        sys.exit()

    # Get train and set training data
    [Xtr, ytr, _, _, Xtst, ytst] = dc.get_all_data_Worker(int(worker_address))
    # Update the labels for the algorithm to classify odd vs even digits
    ytr = np.argmax(ytr, axis=-1)
    filter_even = ytr%2 == 0
    filter_odd = ytr%2 != 0
    ytr[filter_even] = 1
    ytr[filter_odd] = -1
    wn.set_training_data(dataset_name, Xtr, ytr)
    display('WorkerNode loaded %d patterns for training' % wn.NPtr, logger, verbose)


    #---------------  Creating a ML model (Worker side) ---------------------  
    wn.create_model_worker(model_type)
    display('MMLL model %s is ready for training!' %model_type, logger, verbose)
    display('Worker_' + model_type + ' %s is running...' %worker_address, logger, verbose)
    wn.run()
    display('Worker_' + model_type + ' %s: EXIT' %worker_address, logger, verbose)

    # Retrieving and saving the trained model
    display('Retrieving the trained model from WorkerNode', logger, verbose)
    model = wn.get_model()

    # Warning: this save_model utility is only for demo purposes
    output_filename_model = './results/models/Worker_' + str(worker_address) + '_' + dataset_name + '_model.pkl'
    wn.save_model(output_filename_model)

    display('-------------  Obtaining predictions------------------------------------\n', logger, verbose)
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

    output_filename = 'Worker_' + str(worker_address) + '_confusion_matrix_' + dataset_name + '.png'
    title = 'SVM confusion matrix in test set worker'
    plot_cm_seaborn(preds_tst, ytst, classes, title, output_filename, logger, verbose, normalize=True)

