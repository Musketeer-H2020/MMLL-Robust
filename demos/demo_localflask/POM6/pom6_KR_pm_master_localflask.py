# -*- coding: utf-8 -*-
'''
@author:  Angel Navia Vázquez
May 2020
python3 pom6_XC_master_localflask.py --dataset redwine --verbose 1

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
from MMLL.common.tools import eval_regression, display

from MMLL.comms.comms_local_Flask import Comms

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', type=str, default=None, help='The addresses of the workers')
    parser.add_argument('--verbose', type=str, default='1', help='Print on screen if True')
    parser.add_argument('--dataset', type=str, default=None, help='The dataset to be used')
    FLAGS, unparsed = parser.parse_known_args()

    try:
        os.remove('current_taskname.txt')
    except:
        pass

    pom = 6
    Nworkers = 5
    model_type = 'KR_pm'
    dataset_name = FLAGS.dataset
    comms_type = 'localflask'
    master_address = 'ma'
    workers_ids = ['0', '1', '2', '3', '4']
    #Nworkers = 2
    comms = Comms(workers_ids=workers_ids, my_id=master_address)
    comms.name = comms_type

    if FLAGS.verbose == '1':
        verbose = True
    else:
        verbose = False
    logger = Logger('../results/logs/Master.log')
    display('\n\n\nML Model = ' + model_type + '; Dataset name = ' + dataset_name + '\n', logger, verbose=True)

    model_parameters = {}
    regularization = 0.01
    model_parameters.update({'regularization': regularization})
    Nmaxiter = 10
    model_parameters.update({'Nmaxiter': Nmaxiter})
    try:
        # loading centroids
        model_type_c = 'Kmeans_pm'
        input_filename_c = '../results/models/POM' + str(pom) + '_C_' + model_type_c + '_' + dataset_name + '.pkl'
        with open(input_filename_c, 'rb') as f:
            C = pickle.load(f)
        model_parameters.update({'C': C})
        NC = C.shape[0]
        model_parameters.update({'NC': NC})
        Nmaxiter = 10
        model_parameters.update({'Nmaxiter': Nmaxiter})
        display('Master_' + model_type + ': Loaded centroids from %s.' % input_filename_c, logger, True)
    except:
        display('No centroids found at %s' % input_filename_c, logger, verbose)
        display('Master_' + model_type + ': Centroids are needed: run clustering first.', logger, True)
        exit()
    fsigma = 0.2
    model_parameters.update({'fsigma': fsigma})

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
        display('Master_' + model_type + ': Creating MasterNode under POM6', logger, verbose)
    mn = MasterNode(pom, comms, logger, verbose, master_address=master_address)

    # Data connector to get data
    display('Loading data...', logger, verbose=True)
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

    preds_val = model.predict(mn.Xval_b)
    preds_tst = model.predict(mn.Xtst_b)

    NMSE_val = np.linalg.norm(preds_val.ravel() - mn.yval.ravel()) ** 2 / np.linalg.norm(mn.yval) ** 2
    NMSE_tst = np.linalg.norm(preds_tst.ravel() - mn.ytst.ravel()) ** 2 / np.linalg.norm(mn.ytst) ** 2
    display('\n===================================================================', logger, verbose)
    display('Master_' + model_type + ': NMSE on validation set = %s' % str(NMSE_val)[0: 6], logger, verbose)
    display('Master_' + model_type + ': NMSE on test set = %s' % str(NMSE_tst)[0: 6], logger, verbose)
    display('===================================================================\n', logger, verbose)


    eval_regression(pom, model_type, dataset_name, mn.Xval_b, mn.yval, mn.Xtst_b, mn.ytst, preds_val, preds_tst, logger, verbose)
    
    display('Master_' + model_type + ': Terminating all worker nodes.', logger, verbose=True)
    mn.terminate_Workers()

    print('\n---------------------------------------------------------------------')
    print('-------------------- END Machine Learning Procedure ------------------')
    print('----------------------------------------------------------------------\n')