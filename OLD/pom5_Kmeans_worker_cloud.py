# -*- coding: utf-8 -*-
'''
@author:  Angel Navia Vázquez
Jan. 2020
python pom6_Kmeans_pm_worker_cloud.py --id 0 --dataset pima --verbose 1  --platform pycloudmessenger
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', type=str, default=None, help='The addresses of the workers')
    parser.add_argument('--verbose', type=str, default='True', help='Print on screen if True')
    parser.add_argument('--dataset', type=str, default=None, help='The dataset to be used')
    parser.add_argument('--platform', type=str, default='pycloudmessenger', help='The comms plaftorm')
    FLAGS, unparsed = parser.parse_known_args()

    '''
    if FLAGS.id is None or FLAGS.id not in ['0', '1', '2', '3', '4']:
        print("\n ********************************\n STOP: Please provide a valid id value\n *********************************\n")
        print('Usage: python3 pom6_LC_worker.py --id <id>')
        print('Valid id values: 0, 1, 2, 3, 4\n')
        exit()

    if FLAGS.dataset is None:
        print("\n ********************************\n STOP: Please provide a valid dataset name\n *********************************\n")
        print('Usage: python3 pom6_LC_worker.py --dataset <dataset_name>')
        exit()
    '''
    pom = 5
    master_address = 'ma'
    worker_address = str(FLAGS.id)   # This string identifies the worker
    model_type = 'Kmeans'
    dataset_name = FLAGS.dataset
    comms_type = FLAGS.platform
    if FLAGS.verbose == '1':
        verbose = True
    else:
        verbose = False

    logger = Logger('../results/logs/worker_' + str(worker_address) + '.log')
    if verbose:
        display('Worker_' + model_type + ' %s: communicating through %s' % (str(worker_address), comms_type), logger, verbose=True)
    
    if comms_type == 'local_flask':
        from MMLL.comms.comms_local_Flask import Comms
        comms = Comms(my_id=worker_address)
        comms.name = comms_type

    if comms_type == 'pycloudmessenger':
        from MMLL.comms.pycloudmessenger_task_manager import Task_Manager
        # Setting up comms
        credentials_filename = 'musketeer.json'
        tm = Task_Manager(credentials_filename)
        task_name = tm.get_current_task_name()
        print('Current task name: %s' % task_name)

        user_org = 'UC3M'
        user_password = 'Tester'
        comms = tm.create_comms_worker(worker_address, user_password, user_org)
        comms.id = worker_address
        task_name = comms.task_name
        comms.name = 'pycloudmessenger'
        print("Comms created and worker has joined task %s" % task_name)
    '''
    print('STOP AT pom6_LC_worker_cloud')
    import code
    code.interact(local=locals())
    '''
    if verbose:
        display('Worker_' + model_type + ' %s: Creating worker object' % str(worker_address), logger, verbose)
    wn = WorkerNode(pom, comms, logger, verbose=verbose, master_address=master_address)

    # Loading data with the data connector
    data_file = '../input_data/' + dataset_name + '_demonstrator_data.pkl'
    if verbose:
        display('WorkerNode_' + model_type + ' %s: loading data from %s ...' % (str(worker_address), data_file), logger, verbose=True)
    dc = DC(data_file)
    [Xtr, ytr] = dc.get_data_train_Worker(int(worker_address[0]))

    wn.set_training_data(dataset_name, Xtr, ytr, add_bias=False)

    if verbose:
        display('Worker_' + model_type + ' %s: Creating ML model of type %s' % (str(worker_address), model_type), logger, verbose=True)   
    wn.create_model_worker(model_type)

    if verbose:
        display('Worker_' + model_type + ' %s is running...' % str(worker_address), logger, verbose=True)
    wn.run()

    if verbose:
        display('Worker_' + model_type + ' %s: EXIT' % str(worker_address), logger, verbose=True)