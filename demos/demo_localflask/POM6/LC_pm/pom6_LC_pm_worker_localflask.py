# -*- coding: utf-8 -*-
'''
@author:  Angel Navia Vázquez
Jan. 2020
python pom6_LC_pm_worker_localflask.py --id 0 --dataset synth2D --verbose 1

'''
import argparse
import json
import sys
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

# Add higher directory to python modules path.
sys.path.append("../../../../")
from demo_tools.mylogging.logger_v1 import Logger
from demo_tools.data_connectors.Load_from_file import Load_From_File as DC                          # Data connector

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', type=str, default=None, help='The addresses of the workers')
    parser.add_argument('--verbose', type=str, default='1', help='Print on screen if True')
    parser.add_argument('--dataset', type=str, default=None, help='The dataset to be used')
    parser.add_argument('--platform', type=str, default='pycloudmessenger', help='The comms plaftorm')
    FLAGS, unparsed = parser.parse_known_args()
    if FLAGS.verbose == '1':
        verbose = True
    else:
        verbose = False

    pom = 6
    # This string identifies the worker in the real world. Unused by now...
    # pycloudmessenger assigns internal pseudo-ids for communicating
    worker_address = str(FLAGS.id)   
    model_type = 'LC_pm'
    dataset_name = FLAGS.dataset

    logger = Logger('./results/logs/worker_' + str(worker_address) + '.log')
    
    display('===========================================', logger, True)
    display('Creating Worker...', logger, True)

    display('Creating WorkerNode under POM6, communicating through pycloudmessenger', logger, True)
    #########################################
    # Creating Comms object, needed by MMLL
    comms = Comms(my_id=worker_address)
    #########################################
    # Creating Workernode
    wn = WorkerNode(pom, comms, logger, verbose=verbose)
    display('-------------------- Loading dataset %s --------------------------' % dataset_name, logger, True)
    # Warning: this data connector is only designed for the demos. In Musketeer, appropriate data
    # connectors must be provided
    data_file = '../../../../input_data/' + dataset_name + '_demonstrator_data.pkl'
    dc = DC(data_file)
    [Xtr, ytr] = dc.get_data_train_Worker(int(worker_address[0]))
    wn.set_training_data(dataset_name, Xtr, ytr)
    display('WorkerNode loaded %d patterns for train' % wn.NPtr, logger, True)
    #########################################

    #---------------  Creating a ML model (Worker side) ---------------------  
    wn.create_model_worker(model_type)
    display('MMLL model %s is ready for training!' % model_type, logger, True)
    display('Worker_' + model_type + ' %s is running...' % str(worker_address), logger, True)
    wn.run()

    display('Worker_' + model_type + ' %s: EXIT' % str(worker_address), logger, True)