# -*- coding: utf-8 -*-
'''
@author:  Marcos Fernández Díaz
December 2020
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset <dataset> --id <id>

'''
import argparse
import json
import logging
import numpy as np
import sys, os
# Add higher directory to python modules path.
sys.path.append("../../../../")

try:
    from MMLL.nodes.WorkerNode import WorkerNode
    from MMLL.common.MMLL_tools import display
    from MMLL.comms.comms_local_Flask import Comms
except Exception as err:
    if "No module named 'MMLL'" in str(err):
        print('\n' + 80 * '#')
        print('You need to install the MMLL library')
        print('pip install git+https://github.com/Musketeer-H2020/MMLL.git')
        print(80 * '#' + '\n')
    raise

from demo_tools.mylogging.logger_v1 import Logger
from demo_tools.data_connectors.Load_from_file import Load_From_File as DC
from demo_tools.evaluation_tools import create_folders


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
    data_partition_id = FLAGS.id # This integer identifies the data partition used for the worker
    dataset_name = FLAGS.dataset

    # Set basic configuration
    pom = 1
    model_type = 'SVM'
    verbose = False


    # Create the directories for storing relevant outputs if they do not exist
    create_folders("./results/")

    # Setting up the logger
    logger = Logger('./results/logs/Worker_' + str(data_partition_id) + '.log')


    # Load the credentials for pycloudmessenger
    display('===========================================', logger, verbose)
    display('Creating Worker...', logger, verbose)

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

    # Get train and set training data
    [Xtr, ytr] = dc.get_data_train_Worker(int(data_partition_id))
    ytr = np.argmax(ytr, axis=-1)
    filter_even = ytr%2 == 0
    filter_odd = ytr%2 != 0
    ytr[filter_even] = 1
    ytr[filter_odd] = -1
    wn.set_training_data(dataset_name, Xtr, ytr)
    display('WorkerNode loaded %d patterns for train' % wn.NPtr, logger, verbose)


    # Creating a ML model and start training procedure
    wn.create_model_worker(model_type)
    display('MMLL model %s is ready for training!' %model_type, logger, verbose)
    display('Worker_' + model_type + ' %s is running...' %data_partition_id, logger, verbose)
    wn.run()
    display('Worker_' + model_type + ' %s: EXIT' %data_partition_id, logger, verbose)
