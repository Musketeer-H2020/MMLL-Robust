#!/bin/sh
python pom6_LC_worker_cloud.py --id 1workerB --dataset pima --verbose 1  --platform pycloudmessenger &
python pom6_LC_worker_cloud.py --id 2workerC --dataset pima --verbose 1  --platform pycloudmessenger &
python pom6_LC_worker_cloud.py --id 3workerD --dataset pima --verbose 1  --platform pycloudmessenger &
python pom6_LC_worker_cloud.py --id 4workerE --dataset pima --verbose 1  --platform pycloudmessenger &
