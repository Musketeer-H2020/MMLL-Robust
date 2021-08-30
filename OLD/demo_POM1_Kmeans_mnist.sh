#!/bin/sh
python3 pom1_Kmeans_worker.py --id 0 --dataset mnist --verbose False &
python3 pom1_Kmeans_worker.py --id 1 --dataset mnist --verbose False &
python3 pom1_Kmeans_worker.py --id 2 --dataset mnist --verbose False &
python3 pom1_Kmeans_worker.py --id 3 --dataset mnist --verbose False &
python3 pom1_Kmeans_worker.py --id 4 --dataset mnist --verbose False &
python3 pom1_Kmeans_master.py --dataset mnist --verbose False
