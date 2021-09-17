#!/bin/bash

pkill -9 -f "python3 worker_hackaton.py --attack_id"

python3 worker_hackaton.py  --attack_id 1 --user workeruser8 --password workeruser0 --task_name $1 --attack 1 --id 8 &
python3 worker_hackaton.py  --attack_id 2 --user workeruser9 --password workeruser0 --task_name $1 --attack 2 --id 9 
