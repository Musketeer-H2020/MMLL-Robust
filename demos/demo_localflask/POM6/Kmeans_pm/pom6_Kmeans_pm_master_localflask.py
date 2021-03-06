# -*- coding: utf-8 -*-
'''
@author:  Angel Navia Vázquez
May 2020
python3 pom6_Kmeans_pm_master_localflask.py --dataset synth2D --verbose 1

'''
import argparse
import time
import json
import sys, os

# Add higher directory to python modules path.
sys.path.append("../../../../")

try:
    from MMLL.nodes.MasterNode import MasterNode
    from MMLL.common.MMLL_tools import display
    from MMLL.comms.comms_local_Flask import Comms
except:
    print('\n' + 80 * '#')
    print('You need to install the MMLL library')
    print('pip install git+https://github.com/Musketeer-H2020/MMLL.git')
    print(80 * '#' + '\n')
    sys.exit()

from demo_tools.mylogging.logger_v1 import Logger
from demo_tools.data_connectors.Load_from_file import Load_From_File as DC                          # Data connector
from demo_tools.evaluation_tools import eval_clustering, create_folders

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
    model_type = 'Kmeans_pm'
    dataset_name = FLAGS.dataset
    master_address = 'ma'
    workers_ids = ['0', '1', '2', '3', '4']

    #########################################
    display('Creating MasterNode under POM6, communicating through localflask', logger, True)
    # Creating Comms object, needed by MMLL
    comms = Comms(workers_ids=workers_ids, my_id=master_address)
    # Creating Masternode
    mn = MasterNode(pom, comms, logger, verbose)
    display('-------------------- Loading dataset %s --------------------------' % dataset_name, logger, True)
    # Warning: this data connector is only designed for the demos. In Musketeer, appropriate data
    # connectors must be provided
    data_file = '../../../../input_data/' + dataset_name + '_demonstrator_data.pkl'
    dc = DC(data_file)
    #########################################

    input_data_description = None
    if dataset_name == 'synth2D':
        input_data_description = {
                    "NI": 2, 
                    "input_types": [
                    {"type": "num"},
                    {"type": "num"}
                    ]
                    }
  
    #---------------  Creating a ML model (Master side) ---------------------  
    ########################################
    # Parameters depending on the model_type
    ########################################
    if input_data_description is not None:
        model_parameters = {}
        model_parameters.update({'Nmaxiter': 10})
        model_parameters.update({'NC': 8})
        model_parameters.update({'conv_stop': 0.005})
    else:
        display('\n' + '='*50 + '\nERROR: input_data_description is missing\n' + '='*50 + '\n', logger, True)
        sys.exit()

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

    if mn.model_is_trained:

        display('Retrieving the trained model from MasterNode', logger, True)
        model = mn.get_model()
        
        # Warning: this save_model utility is only for demo purposes
        output_filename_model = './results/models/POM' + str(pom) + '_' + model_type + '_' + dataset_name + '_model.pkl'
        mn.save_model(output_filename_model)

        display('-------------  Evaluating --------------------------------------------\n', logger, True)
        # Warning, these evaluation methods are not part of the MMLL library, they are only intended
        # to be used for the demos. Use them at your own risk.   

        display('-------------  Obtaining predictions------------------------------------\n', logger, True)
        try:
            [Xtst, ytst] = dc.get_data_tst()
            preds_tst = model.predict(Xtst)
        except:
            preds_tst = None
            print('ERROR while computing predictions on test data')
        
        eval_clustering(pom, model_type, dataset_name, Xtst, model.c, logger, verbose)

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
