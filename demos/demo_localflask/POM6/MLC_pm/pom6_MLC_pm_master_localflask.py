# -*- coding: utf-8 -*-
'''
@author:  Angel Navia Vázquez
May 2020
python3 pom6_MLC_pm_master_localflask.py --dataset M-mnist --verbose 1

'''
import argparse
import time
import json
import sys, os
import numpy as np

# Add higher directory to python modules path.
sys.path.append("../../../../")

try:
    from MMLL.nodes.MasterNode import MasterNode
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
from demo_tools.data_connectors.Load_from_file import Load_From_File as DC                          # Data connector
from demo_tools.evaluation_tools import eval_multiclass_classification, create_folders

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', type=str, default=None, help='The external names of the workers')
    parser.add_argument('--verbose', type=str, default='1', help='Print messages on screen when True')
    parser.add_argument('--dataset', type=str, default=None, help='The dataset to be used')
    FLAGS, unparsed = parser.parse_known_args()
    if FLAGS.verbose == '1':
        verbose = True
    else:
        verbose = False

    # Create the directories for storing relevant outputs if they do not exist
    create_folders("./results/")

    # Logging is optional, if you do not want to log messages, simply set logger=None
    logger = Logger('./results/logs/Master.log')

    pom = 6
    Nworkers = 5
    model_type = 'MLC_pm'
    dataset_name = FLAGS.dataset
    master_address = 'ma'
    workers_ids = ['0', '1', '2', '3', '4']
    
    display('===========================================', logger, True)
    display('Creating Master... ', logger, True)
    display('Please wait until Master is ready before launching the workers...', logger, True)
    # ==================================================
    # Note: this part creates the task and waits for the workers to join. This code is
    # intended to be used only at the demos, in Musketeer this part must be done in the client. 
    
    
    #########################################
    display('Creating MasterNode under POM6, communicating through pycloudmessenger', logger, True)
    # Creating Comms object, needed by MMLL
    comms = Comms(workers_ids=workers_ids, my_id=master_address)
    # Creating Masternode
    mn = MasterNode(pom, comms, logger, verbose)
    display('-------------------- Loading dataset %s --------------------------' % dataset_name, logger, True)
    # Warning: this data connector is only designed for the demos. In Musketeer, appropriate data
    # connectors must be provided
    data_file = '../../../../input_data/' + dataset_name + '_demonstrator_data.pkl'
    dc = DC(data_file)

    input_data_description = None
    target_data_description = None

    input_data_description = {
                        "NI": 784, 
                        "input_types": [{"type": "num"}] * 784
                        }

    target_data_description = {
                            "NT": 1, 
                            "output_type": [
                            {"type": "cat", "values": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]},
                            ]
                            }
    
    if input_data_description is not None and target_data_description is not None:
        ########################################
        # Parameters depending on the model_type
        ########################################
        model_parameters = {}
        model_parameters.update({'regularization': 0.001})
        model_parameters.update({'Nmaxiter': 10})
        model_parameters.update({'conv_stop': 0.005})
        model_parameters.update({'input_data_description': input_data_description})
        model_parameters.update({'target_data_description': target_data_description})
    else:
        display('\n' + '='*50 + '\nERROR: input_data_description is missing\n' + '='*50 + '\n', logger, True)
        sys.exit()


    #---------------  Creating a ML model (Master side) ---------------------  

    mn.create_model_Master(model_type, model_parameters=model_parameters)
    display('MMLL model %s is ready for training!' % model_type, logger, True)

    # We start the training procedure.
    display('Training the model %s' % model_type, logger, True)
    t_ini = time.time()
    [Xval, yval] = dc.get_data_val()
    mn.fit(Xval=Xval, yval=yval)
    t_end = time.time()
    display('Training is complete: Training time = %s seconds' % str(t_end - t_ini)[0:6], logger, True)
    display('----------------------------------------------------------------------', logger, True)

    display('Retrieving the trained model from MasterNode', logger, True)
    model = mn.get_model()

    if mn.model_is_trained:
        # Warning: this save_model utility is only for demo purposes
        output_filename_model = './results/models/POM' + str(pom) + '_' + model_type + '_' + dataset_name + '_model.pkl'
        mn.save_model(output_filename_model)

        display('-------------  Evaluating --------------------------------------------\n', logger, True)
        # Warning, these evaluation methods are not part of the MMLL library, they are only intended
        # to be used for the demos. Use them at your own risk.   

        display('-------------  Obtaining predictions------------------------------------\n', logger, True)

        display('\n===================================================================', logger, verbose, uselog=False)
        try:
            [Xval, yval] = dc.get_data_val()
            Xval_b = mn.add_bias(Xval)
            preds_val_dict, o_val = model.predict(Xval_b)
            e_val = (yval != o_val).astype(int)
            CE_val = np.mean(e_val) * 100.0
            display('Master_' + model_type + ': CE(%%) on validation set =  %s' % str(CE_val)[0:6], logger, verbose)
        except:
            preds_val = None
            print('ERROR while computing predictions on validation data')
            import code
            code.interact(local=locals())

        try:
            [Xtst, ytst] = dc.get_data_tst()
            Xtst_b = mn.add_bias(Xtst)
            preds_tst_dict, o_tst = model.predict(Xtst_b)
            e_tst = (ytst != o_tst).astype(int)
            CE_tst = np.mean(e_tst) * 100.0
            display('Master_' + model_type + ': CE(%%) on test set =  %s' % str(CE_tst)[0:6], logger, verbose)
        except:
            preds_tst = None
            print('ERROR while computing predictions on test data')
            import code
            code.interact(local=locals())

        classes = model.classes
        eval_multiclass_classification(pom, model_type, dataset_name, Xval_b, yval, Xtst_b, ytst, logger, verbose, mn, classes, preds_val_dict, preds_tst_dict, o_val, o_tst)

        display('Terminating all worker nodes.', logger, True)
        mn.terminate_Workers()

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
