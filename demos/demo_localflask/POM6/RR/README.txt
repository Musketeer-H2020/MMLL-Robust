==================================================================
 Demo execution instructions using localflask under Linux OS
==================================================================

Open seven bash terminal and activate the environment in everyone of them (conda activate demo) and execute any of the following scripts to see the corresponding demo.

Every terminal represents one participant, they can be in different machines.

-------------------------------------------
Execute these lines, one at every terminal:
-------------------------------------------

python local_flask_server.py
python3 pom6_RR_master_localflask.py --dataset ypmsd --verbose 1
python3 pom6_RR_worker_localflask.py --dataset ypmsd --verbose 1 --id 0  
python3 pom6_RR_worker_localflask.py --dataset ypmsd --verbose 1 --id 1 
python3 pom6_RR_worker_localflask.py --dataset ypmsd --verbose 1 --id 2
python3 pom6_RR_worker_localflask.py --dataset ypmsd --verbose 1 --id 3 
python3 pom6_RR_worker_localflask.py --dataset ypmsd --verbose 1 --id 4 

windows

python pom6_RR_master_localflask.py --dataset redwine --verbose 1
python pom6_RR_worker_localflask.py --dataset redwine --verbose 1 --id  
