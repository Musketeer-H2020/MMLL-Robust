# -*- coding: utf-8 -*-
'''
@author:  Angel Navia Vázquez
May 2021
python3 pom6_RR_master_pycloudmessenger.py --dataset redwine --verbose 1

'''
import argparse
import time
import json
import sys, os
import pickle
import numpy as np

# Add higher directory to python modules path.
sys.path.append("../../../../")
sys.path.append("../../../")
from assessment_tools import create_folders_dataset, compute_mem
import logparser

try:
    from MMLL.nodes.MasterNode import MasterNode
    from MMLL.common.MMLL_tools import display
    from MMLL.comms.comms_pycloudmessenger import Comms_master as Comms
except Exception as err:
    if "No module named 'MMLL'" in str(err):
        print('\n' + 80 * '#')
        print('You need to install the MMLL library')
        print('pip install git+https://github.com/Musketeer-H2020/MMLL.git')
        print(80 * '#' + '\n')
    raise

from demo_tools.task_manager_pycloudmessenger import Task_Manager
from demo_tools.mylogging.logger_v1 import Logger
from demo_tools.data_connectors.Load_from_file_Nworkers import Load_From_File as DC                          # Data connector
from demo_tools.evaluation_tools import eval_regression, create_folders
from sklearn.metrics import r2_score
import time

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', type=str, default=None, help='The external names of the workers')
    parser.add_argument('--verbose', type=str, default='1', help='Print messages on screen when True')
    parser.add_argument('--dataset', type=str, default=None, help='The dataset to be used')
    parser.add_argument('--Nworkers', type=str, default=None, help='The number of workers')
    FLAGS, unparsed = parser.parse_known_args()
    if FLAGS.verbose == '1':
        verbose = True
    else:
        verbose = False

    # Create the directories for storing relevant outputs if they do not exist
    create_folders("./results/")

    pom = 6
    Nworkers = int(FLAGS.Nworkers)
    model_type = 'RR'
    dataset_name = FLAGS.dataset
    
    t = time.time()
    seed = int((t - int(t)) * 10000)
    np.random.seed(seed=seed)
    exp_number, log_folder = create_folders_dataset("./results/logs/", dataset_name, Nworkers)
    logger = Logger(log_folder + 'Master.log')

    display('===========================================', logger, True)
    display('Creating Master... ', logger, True)
    display('Please wait until Master is ready before launching the workers...', logger, True)
    # ==================================================
    # Note: this part creates the task and waits for the workers to join. This code is
    # intended to be used only at the demos, in Musketeer this part must be done in the client. 
    credentials_filename = '../../musketeer.json'
    tm = Task_Manager(credentials_filename)
    # We need the aggregator to build comms object
    aggregator = tm.create_master_random_taskname(pom, Nworkers, user_org='UC3M')   
    display('Workers can be launched now!', logger, True)
    display('Waiting for the workers to join task name = %s' % tm.task_name, logger, True)
    tm.wait_for_workers()
    # ==================================================
    
    #########################################
    display('Creating MasterNode under POM6, communicating through pycloudmessenger', logger, True)
    # Creating Comms object, needed by MMLL
    comms = Comms(aggregator)
    # Creating Masternode
    mn = MasterNode(pom, comms, logger, verbose)

    display('-------------------- Loading dataset %s --------------------------' % dataset_name, logger, True)
    # Warning: this data connector is only designed for the demos. In Musketeer, appropriate data
    # connectors must be provided
    data_file = '../../../../input_data/' + dataset_name + '_demonstrator_data.pkl'
    dc = DC(data_file)

    input_data_description = None
    if dataset_name == 'redwine':
        NI = 11
        input_data_description = {
                    "NI": NI, 
                    "input_types": [
                    {"type": "num"}
                    ] * NI
                    }

    if dataset_name == 'blogfeedback_norm':
        NI = 280
        input_data_description = {
                    "NI": NI, 
                    "input_types": [
                    {"type": "num"}
                    ] * NI
                    }

    if dataset_name == 'superconduct_norm':
        NI = 81
        input_data_description = {
                    "NI": NI, 
                    "input_types": [
                    {"type": "num"}
                    ] * NI
                    }

    if dataset_name == 'temperature':
        NI = 5
        input_data_description = {
                    "NI": NI, 
                    "input_types": [
                    {"type": "num"}
                    ] * NI
                    }

    if dataset_name == 'cancer':
        NI = 32
        input_data_description = {
                    "NI": NI, 
                    "input_types": [
                    {"type": "num"}
                    ] * NI
                    }

    if dataset_name == 'abalone':
        NI = 10
        input_data_description = {
                    "NI": NI, 
                    "input_types": [
                    {"type": "num"}
                    ] * NI
                    }

    if dataset_name == 'cadata':
        NI = 8
        input_data_description = {
                    "NI": NI, 
                    "input_types": [
                    {"type": "num"}
                    ] * NI
                    }

  
    #---------------  Creating a ML model (Master side) ---------------------  
    ########################################
    # Parameters depending on the model_type
    ########################################
    if input_data_description is not None:
        model_parameters = {}
        model_parameters.update({'regularization': 0.00000001})
        model_parameters.update({'input_data_description': input_data_description})
    else:
        display('\n' + '='*50 + '\nERROR: input_data_description is missing\n' + '='*50 + '\n', logger, True)
        sys.exit()

    '''
    [Xtr, ytr] = dc.get_data_train_Worker(1, 0)
    model_parameters.update({'Xtr': Xtr})
    model_parameters.update({'ytr': ytr})
    '''
    
    mn.create_model_Master(model_type, model_parameters=model_parameters)
    display('MMLL model %s is ready for training!' % model_type, logger, True)

    # We start the training procedure.
    display('Training the model %s' % model_type, logger, True)
    t_ini = time.time()

    mn.fit()

    t_end = time.time()
    display('Training is completed in %s seconds' % str(t_end - t_ini)[0:6], logger, True)
    display('----------------------------------------------------------------------', logger, True)

    if mn.model_is_trained:
        display('Retrieving the trained model from MasterNode', logger, True)
        model = mn.get_model()
        
        # Saving the model to pickle
        #output_filename_model = mn.save_model(output_filename_model)
        output_filename_model = log_folder +  'POM' + str(pom) + '_' + model_type + '_' + dataset_name + '_model.pkl'
        model.save(output_filename_model)
        print('Model saved in %s'%output_filename_model)

        display('-------------  Evaluating --------------------------------------------\n', logger, True)
        # Warning, these evaluation methods are not part of the MMLL library, they are only intended
        # to be used for the demos. Use them at your own risk.   

        # We check the saved model
        display('Loading the saved model %s'%output_filename_model, logger, True)
        with open(output_filename_model, 'rb') as f:
            model_loaded = pickle.load(f)

        display('-------------  Obtaining predictions------------------------------------\n', logger, True)
        try:
            [Xval, yval] = dc.get_data_val()
            display('MasterNode loaded %d patterns for validation' % Xval.shape[0], logger, True)
            preds_val = model_loaded.predict(Xval)
        except:
            raise

        try:
            [Xtst, ytst] = dc.get_data_tst()
            display('MasterNode loaded %d patterns for test' % Xtst.shape[0], logger, True)
            preds_tst = model_loaded.predict(Xtst)
        except:
            raise

        # ==========================================================
        # Assessment
        MSE_val = np.mean((preds_val - yval)**2)
        MSE_tst = np.mean((preds_tst - ytst)**2)

        R2_val = r2_score(yval, preds_val)
        R2_tst = r2_score(ytst, preds_tst)

        #display('=' * 80, logger, True)

        display('\n', logger, True)
        display('= %s' % str(t_end - t_ini)[0:6].replace('.',','), logger, True)
        display('R2 val = %s' % str(R2_val).replace('.',','), logger, True)
        display('R2 tst = %s' % str(R2_tst).replace('.',','), logger, True)
        #display('= %s' % str(R2_val).replace('.',','), logger, True)
        #display('= %s' % str(R2_tst).replace('.',','), logger, True)
        display('\n', logger, True)

        #display('=' * 80, logger, True)
        # ==========================================================

        #Saving performance data
        output_file = log_folder + 'performance.pkl'
        Train_time = t_end - t_ini
        perf_dict = {}
        perf_dict.update({'Train_time':Train_time})
        perf_dict.update({'MSE_val':MSE_val})
        perf_dict.update({'MSE_tst':MSE_tst})
        perf_dict.update({'R2_val':R2_val})
        perf_dict.update({'R2_tst':R2_tst})

        with open(output_file, 'wb') as f:
            pickle.dump(perf_dict, f)

        display('Terminating all worker nodes.', logger, True)
        mn.terminate_workers()

        time.sleep(30)

        compute_mem(log_folder, Nworkers)

        logparser_results_dict = logparser.parse_directory(log_folder)
        output_file = log_folder + 'logparser_results.pkl'
        with open(output_file, 'wb') as f:
            pickle.dump(logparser_results_dict, f)

        print('\n')
        print('=' * 50)
        print('LOGPARSER OK')
        print('=' * 50)
        print('\n')

        try:
            os.remove('current_taskname.txt')
        except:
            pass

        display('\n---------------------------------------------------------------------', logger, True)
        display('------------------------- END MMLL Procedure -------------------------', logger, True)
        display('----------------------------------------------------------------------\n', logger, True)
    
    else:
        display('\n---------------------------------------------------------------------', logger, True)
        display('------------------------- Training not completed ----------------------', logger, True)
        display('----------------------------------------------------------------------\n', logger, True)






