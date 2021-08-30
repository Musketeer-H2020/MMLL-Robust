# -*- coding: utf-8 -*-
'''
@author:  Angel Navia Vázquez
Jan. 2020
python pom6_XC_worker_localflask.py --id 0 --dataset redwine --verbose 1
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
from MMLL.common.tools import display

from MMLL.comms.comms_local_Flask import Comms

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', type=str, default=None, help='The addresses of the workers')
    parser.add_argument('--verbose', type=str, default='1', help='Print on screen if True')
    parser.add_argument('--dataset', type=str, default=None, help='The dataset to be used')
    FLAGS, unparsed = parser.parse_known_args()

    pom = 6
    master_address = 'ma'
    worker_address = str(FLAGS.id)   # This string identifies the worker
    model_type = 'RR'
    dataset_name = FLAGS.dataset
    comms_type = 'localflask'
    if FLAGS.verbose == '1':
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
    
    wn = WorkerNode(pom, comms, logger, verbose=verbose, master_address=master_address)

    # Loading data with the data connector
    data_file = '../input_data/' + dataset_name + '_demonstrator_data.pkl'
    if verbose:
        display('WorkerNode_' + model_type + ' %s: loading data from %s ...' % (str(worker_address), data_file), logger, verbose=True)
    dc = DC(data_file)
    [Xtr, ytr] = dc.get_data_train_Worker(int(worker_address[0]))

    wn.set_training_data(dataset_name, Xtr, ytr, add_bias=True)

    if verbose:
        display('Worker_' + model_type + ' %s: Creating ML model of type %s' % (str(worker_address), model_type), logger, verbose=True)   
    wn.create_model_worker(model_type)

    if verbose:
        display('Worker_' + model_type + ' %s is running...' % str(worker_address), logger, verbose=True)
    wn.run()

    if verbose:
        display('Worker_' + model_type + ' %s: EXIT' % str(worker_address), logger, verbose=True)