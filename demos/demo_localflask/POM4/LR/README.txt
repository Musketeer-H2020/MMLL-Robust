==================================================================
 Demo execution instructions using localflask under Linux OS
==================================================================

Open eight bash terminal and activate the environment in everyone of them (conda activate demo) and execute any of the following scripts to see the corresponding demo.

Every terminal represents one participant, they can be in different machines.

-------------------------------------------
Execute these lines, one at every terminal:
-------------------------------------------

** NOTE **: POM4 algorithms require some preliminary data processing (encrypting, transmitting deblinding, etc.) among Master, Cryptonode and workers, so it may take a while before the actual learning takes place.   

python local_flask_server.py

python3 pom4_LR_master_localflask.py --dataset redwine --verbose 1

python3 pom4_LR_crypto_localflask.py --verbose 1 --id 5

python3 pom4_LR_worker_localflask.py --dataset redwine --verbose 1 --id 0  
python3 pom4_LR_worker_localflask.py --dataset redwine --verbose 1 --id 1 
python3 pom4_LR_worker_localflask.py --dataset redwine --verbose 1 --id 2 
python3 pom4_LR_worker_localflask.py --dataset redwine --verbose 1 --id 3 
python3 pom4_LR_worker_localflask.py --dataset redwine --verbose 1 --id 4 

windows

python pom4_LR_master_localflask.py --dataset redwine --verbose 1
python pom4_LR_crypto_localflask.py --verbose 1 --id 5
python pom4_LR_worker_localflask.py --dataset redwine --verbose 1 --id 
