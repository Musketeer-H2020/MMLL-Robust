#!/bin/sh
python pom6_LC_worker_cloud.py --id 1workerB --dataset mnist --verbose 1  --platform pycloudmessenger &
python pom6_LC_worker_cloud.py --id 2workerC --dataset mnist --verbose 1  --platform pycloudmessenger &
python pom6_LC_worker_cloud.py --id 3workerD --dataset mnist --verbose 1  --platform pycloudmessenger &
python pom6_LC_worker_cloud.py --id 4workerE --dataset mnist --verbose 1  --platform pycloudmessenger &
