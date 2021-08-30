# -*- coding: utf-8 -*-
'''
@author:  Marcos Fernández Díaz
January 2020
python pom1_data_value_estimation.py --dataset <dataset> --num_workers <num_workers>

'''
import argparse
import time
import logging
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

# To be imported from demo_tools 
from demo_tools.mylogging.logger_v1 import Logger
from demo_tools.data_connectors.Load_from_file import Load_From_File as DC
from demo_tools.evaluation_tools import create_folders


# Set up logger
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, default=None, help='The dataset to be used')
    parser.add_argument('--num_workers', type=int, default=2, choices=[1, 2, 3, 4, 5], help='The dataset to be used')

    FLAGS, unparsed = parser.parse_known_args()
    dataset_name = FLAGS.dataset
    num_workers = FLAGS.num_workers

    # Set basic configuration
    pom = 1
    Nworkers = 5
    model_type = 'SVM'
    verbose = False

    # The master must know the workers ids
    workers_ids = [str(worker) for worker in range(num_workers)]
    Nworkers = len(workers_ids)
    master_address = 'ma'


    # Create the directories for storing relevant outputs if they do not exist
    create_folders("./results/")

    # Logging is optional, if you do not want to log messages, simply set logger=None
    logger = Logger('./results/logs/Master.log')


    # Task definition
    model_parameters = {}
    Nmaxiter = 4
    NC = 200
    tolerance = 0.001
    sigma = 2.55
    C = 1
    NmaxiterGD = 10
    eta = 0.05
    model_parameters.update({'Nmaxiter': Nmaxiter, 'NC': NC, 'tolerance': tolerance, 'sigma': sigma, 'C': C, 'NmaxiterGD': NmaxiterGD, 'eta': eta})
   
    
    # Creating the comms object
    display('Creating MasterNode under POM %d, communicating through local flask' %pom, logger, verbose)
    comms = Comms(workers_ids=workers_ids, my_id=master_address)

    # Creating Masternode
    mn = MasterNode(pom, comms, logger, verbose)
    display('-------------------- Loading dataset %s --------------------------' %dataset_name, logger, verbose)

    # Load data
    # Warning: this data connector is only designed for the demos. In Musketeer, appropriate data
    # connectors must be provided
    data_file = '../../../../input_data/' + dataset_name + '_demonstrator_data.pkl'
    try:
        dc = DC(data_file)
    except:
        display('Error - The file ' + dataset_name + '_demonstrator_data.pkl does not exist. Please download it from Box and put it under the following path: "' + os.path.abspath(os.path.join("","../../../../input_data/")) + '"', logger, verbose)
        sys.exit()


    # Input and output data description needed for preprocessing
    input_data_description = None
    if dataset_name in ["income_dv_small"]:
        input_data_description = {
                            "NI": 107, 
                            "input_types": [{"type": "num"}] * 107
                            }

        target_data_description= {
        "NT": 1, 
        "output_types": [
        {"type": "bin", "name": "income", "definition": ">50K, <=50K"}
        ]
        }


    # Creating a ML model
    mn.create_model_Master(model_type, model_parameters=model_parameters)
    display('MMLL model %s is ready for training!' % model_type, logger, verbose)

    # Get validation data
    [Xval, yval] = dc.get_data_val()
    yval = np.argmax(yval, axis=-1)
    filter_even = yval%2 == 0
    filter_odd = yval%2 != 0
    yval[filter_even] = 1
    yval[filter_odd] = -1
    dv, best_workers = mn.get_data_value_aposteriori(Xval, yval, baseline_auc=0.7)

    for kworker in range(Nworkers):
        display('Data value for worker %s is %f' % (best_workers[kworker], dv[kworker]), logger, verbose)


    display('----------------------------------------------------------------------', logger, verbose)
    display('---------------- Data value estimation completed  --------------------', logger, verbose)
    display('----------------------------------------------------------------------\n', logger, verbose)

    display('Terminating all worker nodes.', logger, verbose)
    mn.terminate_workers()



