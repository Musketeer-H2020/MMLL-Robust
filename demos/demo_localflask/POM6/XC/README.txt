==================================================================
 Demo execution instructions using localflask under Linux OS
==================================================================

Open seven bash terminal and activate the environment in everyone of them (conda activate demo) and execute any of the following scripts to see the corresponding demo.

Every terminal represents one participant, they can be in different machines.

-------------------------------------------
Execute these lines, one at every terminal:
-------------------------------------------

python local_flask_server.py
python3 pom6_LC_pm_master_localflask.py --dataset Bmnist --verbose 1
python pom6_LC_pm_worker_localflask.py --id 0 --dataset Bmnist --verbose 1 
python pom6_LC_pm_worker_localflask.py --id 1 --dataset Bmnist --verbose 1 
python pom6_LC_pm_worker_localflask.py --id 2 --dataset Bmnist --verbose 1 
python pom6_LC_pm_worker_localflask.py --id 3 --dataset Bmnist --verbose 1 
python pom6_LC_pm_worker_localflask.py --id 4 --dataset Bmnist --verbose 1 


=====================================================
Normalization Demo: training LC_pm with pima raw data
=====================================================

python local_flask_server.py
python3 pom6_LC_pm_master_localflask_normalization.py --dataset pima_raw --verbose 1
python pom6_LC_pm_worker_localflask.py --id 0 --dataset pima_raw --verbose 1 
python pom6_LC_pm_worker_localflask.py --id 1 --dataset pima_raw --verbose 1 
python pom6_LC_pm_worker_localflask.py --id 2 --dataset pima_raw --verbose 1 
python pom6_LC_pm_worker_localflask.py --id 3 --dataset pima_raw --verbose 1 
python pom6_LC_pm_worker_localflask.py --id 4 --dataset pima_raw --verbose 1 
