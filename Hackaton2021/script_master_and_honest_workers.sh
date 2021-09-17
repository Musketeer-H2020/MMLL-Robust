#!/bin/bash

pkill -9 -f "python3 master_hackaton.py"
pkill -9 -f "python3 worker_hackaton.py"

python3 master_hackaton.py --user masteruser --password masteruser --task_name $1 --scenario 1 &

sleep 15

python3 worker_hackaton.py --user workeruser0 --password workeruser0 --task_name $1 --id 0 &
python3 worker_hackaton.py --user workeruser1 --password workeruser0 --task_name $1 --id 1 &
python3 worker_hackaton.py --user workeruser2 --password workeruser0 --task_name $1 --id 2 &
python3 worker_hackaton.py --user workeruser3 --password workeruser0 --task_name $1 --id 3 &
python3 worker_hackaton.py --user workeruser4 --password workeruser0 --task_name $1 --id 4 &
python3 worker_hackaton.py --user workeruser5 --password workeruser0 --task_name $1 --id 5 &
python3 worker_hackaton.py --user workeruser6 --password workeruser0 --task_name $1 --id 6 &
python3 worker_hackaton.py --user workeruser7 --password workeruser0 --task_name $1 --id 7 
