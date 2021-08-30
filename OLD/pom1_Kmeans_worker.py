# -*- coding: utf-8 -*-
'''
@author:  Tree Technologies
Jan. 2020

python pom1_Kmeans_worker.py --id 0 --dataset mnist --verbose True

'''
'''
import json
'''
import argparse
# Add higher directory to python modules path.
import sys
sys.path.append("..")
from MMLL.nodes.WorkerNode import WorkerNode
from MMLL.data_connectors.Load_from_file import Load_From_File as DC                          # Data connector
from MMLL.mylogging.logger_v1 import Logger
from MMLL.comms.comms_local_Flask import Comms
from MMLL.common.tools import display, Kmeans_plot


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', type=str, default=None, help='The addresses of the workers')
    parser.add_argument('--verbose', type=str, default='True', help='Print on screen if True')
    parser.add_argument('--dataset', type=str, default=None, help='The dataset to be used')
    FLAGS, unparsed = parser.parse_known_args()

    if FLAGS.id is None or FLAGS.id not in ['0', '1', '2', '3', '4']:
        print("\n ********************************\n STOP: Please provide a valid id value\n *********************************\n")
        print('Usage: python3 demo1_worker.py --id <id>')
        print('Valid id values: 0, 1, 2, 3, 4\n')
        exit()

    pom = 1
    master_address = 'ma'
    worker_address = str(FLAGS.id)   # This string identifies the worker
    model_type = 'Kmeans'
    dataset_name = FLAGS.dataset
    comms_type = 'localflask'
    if FLAGS.verbose == 'True':
        verbose = True
    else:
        verbose = False

    logger = Logger('../results/logs/worker_' + str(worker_address) + '.log')
    if verbose:
        display('Worker_' + model_type + ' %s: communicating through %s' % (str(worker_address), comms_type), logger, verbose=True)
    comms = Comms(my_id=worker_address)
    comms.name = comms_type

    if verbose:
        display('Worker_' + model_type + ' %s: Creating worker object' % str(worker_address), logger, verbose)
    wn = WorkerNode(pom, worker_address, comms, logger, verbose=verbose, master_address=master_address)

    # Loading data with the data connector
    data_file = '../input_data/' + dataset_name + '_demonstrator_data.pkl'
    if verbose:
        display('WorkerNode_' + model_type + ' %s: loading data from %s ...' % (str(worker_address), data_file), logger, verbose=True)
    dc = DC(data_file)

    [Xtr, ytr, Xval, yval, Xtst, ytst] = dc.get_all_data_Worker(int(worker_address))

    wn.set_training_data(dataset_name, Xtr, ytr, add_bias=False)
    wn.set_validation_data(dataset_name, Xval, yval, add_bias=False)
    wn.set_test_data(dataset_name, Xtst, ytst, add_bias=False)

    if verbose:
        display('Worker_' + model_type + ' %s: Creating ML model of type %s' % (str(worker_address), model_type), logger, verbose=True)   
    wn.create_model_worker(model_type)

    if verbose:
        display('Worker_' + model_type + ' %s is running...' % str(worker_address), logger, verbose=True)
    wn.run()

    if verbose:
        display('Worker_' + model_type + ' %s: EXIT' % str(worker_address), logger, verbose=True)

    # Retrieving and saving the trained model
    print('\n---------------------------------------------------------------------')
    print('------------- Saving the trained Machine Learning Model----------------')
    print('---------------------------------------------------------------------')
    model = wn.get_model()
    wn.save_model()
    print('---------------------------------------------------------------------\n')

    preds_val = model.predict(wn.Xval_b)
    preds_tst = model.predict(wn.Xtst_b)

    Kmeans_plot(Xtst, preds_tst, 'Kmeans clustering with 2 PCA components in test set worker', model_type, dataset_name, logger, verbose)
