# -*- coding: utf-8 -*-
'''
@author:  Marcos Fernandez Diaz
October 2020

Example of use: python pom3_Kmeans_worker_local_flask.py --id <id>

Parameters:
    - id: Integer representing the partition of data to be used by the worker. Each worker should use a different partition, possible values are 0 to 4.

'''


# Import general modules
import argparse
import sys, os
import logging

# Add higher directory to python modules path.
sys.path.append("../../../../")

# To be imported from MMLL (pip installed)
from MMLL.comms.comms_local_Flask import Comms
from MMLL.nodes.WorkerNode import WorkerNode

# To be imported from demo_tools
from demo_tools.data_connectors.Load_from_file import Load_From_File as DC
from demo_tools.mylogging.logger_v1 import Logger
from demo_tools.evaluation_tools import display, Kmeans_plot, create_folders


# Set up logger
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', type=int, default=None, help='The addresses of the workers')

    FLAGS, unparsed = parser.parse_known_args()
    worker_address = FLAGS.id

    if FLAGS.id is None or FLAGS.id not in [0, 1, 2, 3, 4]:
        display('STOP: Please provide a valid id value', logger, False)
        display('Usage: python pom3_Kmeans_worker_local_flask.py --id <id>', logger, False)
        display('Valid id values: 0, 1, 2, 3, 4', logger, False)
        exit()

    # Set basic configuration
    dataset_name = 'pima'
    verbose = False
    pom = 3
    model_type = 'Kmeans'


    # Create the directories for storing relevant outputs if they do not exist
    create_folders("./results/")

    # Setting up the logger
    logger = Logger('./results/logs/Worker_' + str(worker_address) + '.log')

    # Creating the comms object
    display('===========================================', logger, verbose)
    display('Creating WorkerNode under POM %d, communicating through local flask' %pom, logger, verbose)
    comms = Comms(my_id=worker_address)

    # Creating Workernode
    wn = WorkerNode(pom, comms, logger, verbose)
    display('-------------------- Loading dataset %s --------------------------' % dataset_name, logger, verbose)

    # Load data
    # Warning: this data connector is only designed for the demos. In Musketeer, appropriate data connectors must be provided
    data_file = '../../../../input_data/' + dataset_name + '_demonstrator_data.pkl'
    try:
        dc = DC(data_file)
    except:
        display('Error - The file ' + dataset_name + '_demonstrator_data.pkl does not exist. Please download it from Box and put it under the following path: "' + os.path.abspath(os.path.join("","../../../../input_data/")) + '"', logger, verbose)
        sys.exit()

    # Get train/test data and set training data
    [Xtr, ytr, _, _, Xtst, ytst] = dc.get_all_data_Worker(int(worker_address))
    wn.set_training_data(dataset_name, Xtr, ytr)
    display('WorkerNode loaded %d patterns for training' % wn.NPtr, logger, verbose)

    # Creating a ML model and start training procedure
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

    # Making predictions on test data
    display('-------------  Obtaining predictions------------------------------------\n', logger, verbose)
    normalizer = wn.get_preprocessors()
    if normalizer is not None:
        Xtst = normalizer.transform(Xtst)
    preds_tst = model.predict(Xtst)

    # Evaluating the results
    display('-------------  Evaluating --------------------------------------------\n', logger, verbose)
    # Warning, these evaluation methods are not part of the MMLL library, they are only intended to be used for the demos. Use them at your own risk.
    output_filename = 'Worker_' + str(worker_address) + '_clusters_' + dataset_name + '.png'
    title = 'Kmeans clustering with 2 PCA components in test set worker'
    Kmeans_plot(Xtst, preds_tst, title, output_filename, logger, verbose)
