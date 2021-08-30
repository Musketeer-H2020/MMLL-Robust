#!/bin/sh
python pom6_Kmeans_pm_worker_cloud.py --id 1workerB --dataset synth2D --verbose 1  --platform pycloudmessenger &
python pom6_Kmeans_pm_worker_cloud.py --id 2workerC --dataset synth2D --verbose 1  --platform pycloudmessenger &
python pom6_Kmeans_pm_worker_cloud.py --id 3workerD --dataset synth2D --verbose 1  --platform pycloudmessenger &
python pom6_Kmeans_pm_worker_cloud.py --id 4workerE --dataset synth2D --verbose 1  --platform pycloudmessenger &
