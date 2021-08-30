# -*- coding: utf-8 -*-
'''
@author:  Angel Navia Vázquez
May 2020
python3 pom5_Kmeans_master_cloud.py --dataset synth2D --verbose 1 --platform pycloudmessenger
'''
import argparse
import time
import numpy as np
import pickle
import random, string
# Add higher directory to python modules path.
import sys, os
sys.path.append("..")
from MMLL.nodes.MasterNode import MasterNode
from MMLL.data_connectors.Load_from_file import Load_From_File as DC                          # Data connector
from MMLL.mylogging.logger_v1 import Logger
from MMLL.common.tools import eval_clustering, display


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', type=str, default=None, help='The addresses of the workers')
    parser.add_argument('--verbose', type=int, default=1, help='Print on screen if True')
    parser.add_argument('--dataset', type=str, default=None, help='The dataset to be used')
    parser.add_argument('--platform', type=str, default='pycloudmessenger', help='The comms plaftorm')
    FLAGS, unparsed = parser.parse_known_args()

    try:
        os.remove('current_taskname.txt')
    except:
        pass

    pom = 5
    master_address = 'ma'
    # The master must know the workers ids
    workers_ids = ['0', '1', '2', '3', '4']
    Nworkers = len(workers_ids)
    #Nworkers = 2

    model_type = 'Kmeans'
    dataset_name = FLAGS.dataset
    comms_type = FLAGS.platform
    crypt_library = 'phe'
    use_crypt = True

    if comms_type == 'local_flask':
        from MMLL.comms.comms_local_Flask import Comms
        comms = Comms(workers_ids=workers_ids, my_id=master_address)
        comms.name = comms_type

    if comms_type == 'pycloudmessenger':
        from MMLL.comms.pycloudmessenger_task_manager import Task_Manager
        # Setting up comms
        credentials_filename = 'musketeer.json'
        tm = Task_Manager(credentials_filename)

        comms = tm.create_comms_master_random_taskname(pom, Nworkers)
        comms.name = comms_type
        
        task_name = comms.task_name
        print('Task name = %s' % task_name)
        
        print('Waiting for the workers to join')
        workers_addresses_cloud = tm.wait_for_workers(Nworkers)
        comms.workers_addresses_cloud = workers_addresses_cloud
        comms.workers_ids = workers_ids  # 0, 1, 2, etc.

    model_parameters = {}
    Nmaxiter = 10
    model_parameters.update({'Nmaxiter': Nmaxiter})
    NC = 8
    model_parameters.update({'NC': NC})
    conv_stop = 0.005
    model_parameters.update({'conv_stop': conv_stop})

    task_definition = {'NI': 2, 'inputs_type': ['float', 'float']}
    Nmaxiter = 20
    model_parameters.update({'task_definition': task_definition})

    if crypt_library == 'phe':
        key_size = 512
        from MMLL.crypto.crypt_PHE import Crypto as CR
        cr = CR(key_size=key_size)
        model_parameters.update({'cr': cr})

    if FLAGS.verbose == '1':
        verbose = True
    else:
        verbose = False

    logger = Logger('../results/logs/Master.log')
    display('\n\n\nML Model = ' + model_type + '; Dataset name = ' + dataset_name + '\n', logger, verbose=True)
    display('Loading data...', logger, verbose=True)

    if verbose:
        print('\n---------------------------------------------------------------------')
        print('-------------------- Loading data at Master --------------------------')
        print('----------------------------------------------------------------------\n')

    ########################################
    # Parameters depending on the model_type
    ########################################
    if verbose:
        display('Master_' + model_type + ': communicating through %s' % comms_type, logger, verbose=True)

    if verbose:
        display('Master_' + model_type + ': Creating MasterNode under POM5', logger, verbose)
    mn = MasterNode(pom, comms, logger, verbose, master_address=master_address)

    # Data connector to get data
    if verbose:
        display('Master_' + model_type + ': Loading Data Connector', logger, verbose)
    data_file = '../input_data/' + dataset_name + '_demonstrator_data.pkl'
    dc = DC(data_file)
    [Xval, yval] = dc.get_data_val()
    [Xtst, ytst] = dc.get_data_tst()

    mn.set_validation_data(dataset_name, Xval, yval, add_bias=False)
    mn.set_test_data(dataset_name, Xtst, ytst, add_bias=False)

    if verbose:
        display('Master_' + model_type + ': Loaded %d patterns for validation' % mn.NPval, logger, verbose=True)
        display('Master_' + model_type + ': Loaded %d patterns for test' % mn.NPtst, logger, verbose=True)

    # Creating a ML model
    if verbose:
        display('Master_' + model_type + ': Activating task: ' + model_type, logger, verbose=True)
    mn.create_model_Master(model_type, model_parameters=model_parameters)
    mn.MasterMLmodel.Xval_b = mn.Xval_b
    mn.MasterMLmodel.yval = mn.yval

    if verbose:
        print('\n============================================')
        print('MMLL is ready for training.')
        print('============================================')

    # We start the training procedure.
    t_ini = time.time()
    print('\n---------------------------------------------------------------------')
    display('Master_' + model_type + ': Training the model', logger, verbose=True)
    mn.fit()
    display('Master_' + model_type + ': Training complete.', logger, verbose=True)
    t_end = time.time()
    display('Master_' + model_type + ': Training time = %s seconds' % str(t_end - t_ini)[0:6], logger, verbose=True)
    print('----------------------------------------------------------------------')

    # Retrieving and saving the trained model
    print('\n---------------------------------------------------------------------')
    print('------------- Saving the trained Machine Learning Model----------------')
    print('---------------------------------------------------------------------')
    model = mn.get_model()
    mn.save_model()
    print('---------------------------------------------------------------------\n')

    eval_clustering(pom, model_type, dataset_name, mn.Xtst_b, model.c, logger, verbose)

    display('Master_' + model_type + ': Terminating all worker nodes.', logger, verbose=True)
    mn.terminate_Workers()

    print('\n---------------------------------------------------------------------')
    print('-------------------- END Machine Learning Procedure ------------------')
    print('----------------------------------------------------------------------\n')