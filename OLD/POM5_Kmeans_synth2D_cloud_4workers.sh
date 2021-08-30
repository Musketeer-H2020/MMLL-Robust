#!/bin/sh
python pom5_Kmeans_worker_cloud.py --id 1workerB --dataset synth2D --verbose 1  --platform pycloudmessenger &
python pom5_Kmeans_worker_cloud.py --id 2workerC --dataset synth2D --verbose 1  --platform pycloudmessenger &
python pom5_Kmeans_worker_cloud.py --id 3workerD --dataset synth2D --verbose 1  --platform pycloudmessenger &
python pom5_Kmeans_worker_cloud.py --id 4workerE --dataset synth2D --verbose 1  --platform pycloudmessenger &
