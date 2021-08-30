# -*- coding: utf-8 -*-
'''
@author:  Tree Technologies
March 2020

python3 pom1_Kmeans_master.py --dataset mnist --verbose True 

'''
import argparse
import time
import numpy as np

# Add higher directory to python modules path.
import sys
sys.path.append("..")
from MMLL.nodes.MasterNode import MasterNode
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

    pom = 2
    master_address = 'ma'
    # The master must know the workers ids
    workers_ids = ['0', '1', '2', '3', '4']
    Nworkers = len(workers_ids)
    model_type = 'Kmeans'
    dataset_name = FLAGS.dataset
    comms_type = 'localflask'

    model_parameters = {}
    Nmaxiter = 10
    NC=2
    tolerance=0.001
    model_parameters.update({'Nmaxiter': Nmaxiter, 'NC': NC, 'tolerance': tolerance})

    if FLAGS.verbose == 'True':
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
    comms = Comms(workers_ids=workers_ids, my_id=master_address)
    comms.name = comms_type

    if verbose:
        display('Master_' + model_type + ': Creating MasterNode under POM6', logger, verbose)
    mn = MasterNode(pom, comms, logger, verbose, master_address=master_address)


    # Creating a ML model
    if verbose:
        display('Master_' + model_type + ': Activating task: ' + model_type, logger, verbose=True)
    mn.create_model_Master(model_type, model_parameters=model_parameters)


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

    
    display('Master_' + model_type + ': Terminating all worker nodes.', logger, verbose=True)
    mn.terminate_Workers()

    print('\n---------------------------------------------------------------------')
    print('-------------------- END Machine Learning Procedure ------------------')
    print('----------------------------------------------------------------------\n')

