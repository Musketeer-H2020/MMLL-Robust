==================================================================
 Demo execution instructions using localflask under Linux OS
==================================================================

Open seven bash terminal and activate the environment in everyone of them (conda activate demo) and execute any of the following scripts to see the corresponding demo.

Every terminal represents one participant, they can be in different machines.

-------------------------------------------
Execute these lines, one at every terminal:
-------------------------------------------

python local_flask_server.py
python3 pom5_LR_master_localflask.py --dataset redwine --verbose 1
python3 pom5_LR_worker_localflask.py --id 0 --dataset redwine --verbose 1 
python3 pom5_LR_worker_localflask.py --id 1 --dataset redwine --verbose 1 
python3 pom5_LR_worker_localflask.py --id 2 --dataset redwine --verbose 1 
python3 pom5_LR_worker_localflask.py --id 3 --dataset redwine --verbose 1 
python3 pom5_LR_worker_localflask.py --id 4 --dataset redwine --verbose 1 


windows

python pom5_LR_master_localflask.py --dataset redwine --verbose 1
python pom5_LR_worker_localflask.py --dataset redwine --verbose 1 --id 
