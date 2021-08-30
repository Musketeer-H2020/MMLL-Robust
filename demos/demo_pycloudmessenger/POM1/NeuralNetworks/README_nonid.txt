############# NON ID experiments  #######################

#########################################################
                    mnist_binclass
#########################################################

----------------------   4 workers  --------------------------


taskset --cpu-list 5 python3 pom1_NN_master_pycloudmessenger_nonid.py --user UC3Mm_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 4 &

taskset --cpu-list 1 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M0_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 4 --id 0 &

taskset --cpu-list 2 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M1_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 4  --id 1 & 

taskset --cpu-list 3 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M2_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 4 --id 2 & 

taskset --cpu-list 4 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M3_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 4 --id 3 & 

----------------------   8 workers  --------------------------

taskset --cpu-list 9 python3 pom1_NN_master_pycloudmessenger_nonid.py --user UC3Mm_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 8 &

taskset --cpu-list 1 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M0_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 8 --id 0 &

taskset --cpu-list 2 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M1_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 8  --id 1 & 

taskset --cpu-list 3 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M2_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 8 --id 2 & 

taskset --cpu-list 4 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M3_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 8 --id 3 & 

taskset --cpu-list 5 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M4_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 8 --id 4 &

taskset --cpu-list 6 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M5_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 8  --id 5 & 

taskset --cpu-list 7 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M6_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 8 --id 6 & 

taskset --cpu-list 8 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M7_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 8 --id 7 & 

----------------------   16 workers  --------------------------

taskset --cpu-list 17 python3 pom1_NN_master_pycloudmessenger_nonid.py --user UC3Mm_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 16 &

taskset --cpu-list 1 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M0_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 16 --id 0 &

taskset --cpu-list 2 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M1_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 16  --id 1 & 

taskset --cpu-list 3 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M2_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 16 --id 2 & 

taskset --cpu-list 4 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M3_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 16 --id 3 & 

taskset --cpu-list 5 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M4_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 16 --id 4 &

taskset --cpu-list 6 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M5_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 16  --id 5 & 

taskset --cpu-list 7 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M6_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 16 --id 6 & 

taskset --cpu-list 8 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M7_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 16 --id 7 & 

taskset --cpu-list 9 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M8_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 16 --id 8 &

taskset --cpu-list 10 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M9_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 16  --id 9 & 

taskset --cpu-list 11 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M10_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 16 --id 10 & 

taskset --cpu-list 12 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M11_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 16 --id 11 & 

taskset --cpu-list 13 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M12_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 16 --id 12 &

taskset --cpu-list 14 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M13_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 16  --id 13 & 

taskset --cpu-list 15 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M14_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 16 --id 14 & 

taskset --cpu-list 16 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M15_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 16 --id 15 & 


----------------------   32 workers  --------------------------

********   Máquina 1

taskset --cpu-list 17 python3 pom1_NN_master_pycloudmessenger_nonid.py --user UC3Mm_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32 &

taskset --cpu-list 1 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M0_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32 --id 0 &

taskset --cpu-list 2 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M1_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32  --id 1 & 

taskset --cpu-list 3 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M2_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32 --id 2 & 

taskset --cpu-list 4 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M3_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32 --id 3 & 

taskset --cpu-list 5 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M4_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32 --id 4 &

taskset --cpu-list 6 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M5_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32  --id 5 & 

taskset --cpu-list 7 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M6_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32 --id 6 & 

taskset --cpu-list 8 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M7_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32 --id 7 & 

taskset --cpu-list 9 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M8_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32 --id 8 &

taskset --cpu-list 10 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M9_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32  --id 9 & 

taskset --cpu-list 11 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M10_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32 --id 10 & 

taskset --cpu-list 12 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M11_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32 --id 11 & 

taskset --cpu-list 13 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M12_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32 --id 12 &

taskset --cpu-list 14 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M13_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32  --id 13 & 

taskset --cpu-list 15 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M14_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32 --id 14 & 

taskset --cpu-list 16 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M15_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32 --id 15 & 

********   Máquina 2

taskset --cpu-list 1 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M16_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32 --id 16 &

taskset --cpu-list 2 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M17_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32  --id 17 & 

taskset --cpu-list 3 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M18_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32 --id 18 & 

taskset --cpu-list 4 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M19_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32 --id 19 & 

taskset --cpu-list 5 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M20_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32 --id 20 &

taskset --cpu-list 6 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M21_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32  --id 21 & 

taskset --cpu-list 7 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M22_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32 --id 22 & 

taskset --cpu-list 8 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M23_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32 --id 23 & 

taskset --cpu-list 9 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M24_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32 --id 24 &

taskset --cpu-list 10 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M25_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32  --id 25 & 

taskset --cpu-list 11 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M26_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32 --id 26 & 

taskset --cpu-list 12 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M27_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32 --id 27 & 

taskset --cpu-list 13 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M28_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32 --id 28 &

taskset --cpu-list 14 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M29_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32  --id 29 & 

taskset --cpu-list 15 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M30_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32 --id 30 & 

taskset --cpu-list 16 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M31_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset mnist_binclass --Nworkers 32 --id 31 & 


#########################################################
                        ijcnn1
#########################################################

----------------------   4 workers  --------------------------


taskset --cpu-list 5 python3 pom1_NN_master_pycloudmessenger_nonid.py --user UC3Mm_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 4 &

taskset --cpu-list 1 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M0_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 4 --id 0 &

taskset --cpu-list 2 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M1_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 4  --id 1 & 

taskset --cpu-list 3 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M2_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 4 --id 2 & 

taskset --cpu-list 4 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M3_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 4 --id 3 & 

----------------------   8 workers  --------------------------

taskset --cpu-list 9 python3 pom1_NN_master_pycloudmessenger_nonid.py --user UC3Mm_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 8 &

taskset --cpu-list 1 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M0_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 8 --id 0 &

taskset --cpu-list 2 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M1_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 8  --id 1 & 

taskset --cpu-list 3 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M2_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 8 --id 2 & 

taskset --cpu-list 4 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M3_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 8 --id 3 & 

taskset --cpu-list 5 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M4_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 8 --id 4 &

taskset --cpu-list 6 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M5_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 8  --id 5 & 

taskset --cpu-list 7 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M6_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 8 --id 6 & 

taskset --cpu-list 8 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M7_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 8 --id 7 & 

----------------------   16 workers  --------------------------

taskset --cpu-list 17 python3 pom1_NN_master_pycloudmessenger_nonid.py --user UC3Mm_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 16 &

taskset --cpu-list 1 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M0_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 16 --id 0 &

taskset --cpu-list 2 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M1_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 16  --id 1 & 

taskset --cpu-list 3 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M2_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 16 --id 2 & 

taskset --cpu-list 4 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M3_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 16 --id 3 & 

taskset --cpu-list 5 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M4_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 16 --id 4 &

taskset --cpu-list 6 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M5_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 16  --id 5 & 

taskset --cpu-list 7 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M6_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 16 --id 6 & 

taskset --cpu-list 8 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M7_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 16 --id 7 & 

taskset --cpu-list 9 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M8_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 16 --id 8 &

taskset --cpu-list 10 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M9_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 16  --id 9 & 

taskset --cpu-list 11 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M10_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 16 --id 10 & 

taskset --cpu-list 12 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M11_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 16 --id 11 & 

taskset --cpu-list 13 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M12_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 16 --id 12 &

taskset --cpu-list 14 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M13_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 16  --id 13 & 

taskset --cpu-list 15 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M14_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 16 --id 14 & 

taskset --cpu-list 16 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M15_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 16 --id 15 & 

----------------------   32 workers  --------------------------

********   Máquina 1

taskset --cpu-list 17 python3 pom1_NN_master_pycloudmessenger_nonid.py --user UC3Mm_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32 &

taskset --cpu-list 1 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M0_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32 --id 0 &

taskset --cpu-list 2 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M1_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32  --id 1 & 

taskset --cpu-list 3 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M2_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32 --id 2 & 

taskset --cpu-list 4 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M3_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32 --id 3 & 

taskset --cpu-list 5 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M4_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32 --id 4 &

taskset --cpu-list 6 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M5_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32  --id 5 & 

taskset --cpu-list 7 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M6_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32 --id 6 & 

taskset --cpu-list 8 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M7_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32 --id 7 & 

taskset --cpu-list 9 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M8_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32 --id 8 &

taskset --cpu-list 10 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M9_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32  --id 9 & 

taskset --cpu-list 11 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M10_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32 --id 10 & 

taskset --cpu-list 12 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M11_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32 --id 11 & 

taskset --cpu-list 13 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M12_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32 --id 12 &

taskset --cpu-list 14 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M13_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32  --id 13 & 

taskset --cpu-list 15 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M14_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32 --id 14 & 

taskset --cpu-list 16 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M15_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32 --id 15 & 

********   Máquina 2

taskset --cpu-list 1 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M16_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32 --id 16 &

taskset --cpu-list 2 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M17_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32  --id 17 & 

taskset --cpu-list 3 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M18_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32 --id 18 & 

taskset --cpu-list 4 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M19_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32 --id 19 & 

taskset --cpu-list 5 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M20_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32 --id 20 &

taskset --cpu-list 6 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M21_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32  --id 21 & 

taskset --cpu-list 7 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M22_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32 --id 22 & 

taskset --cpu-list 8 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M23_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32 --id 23 & 

taskset --cpu-list 9 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M24_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32 --id 24 &

taskset --cpu-list 10 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M25_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32  --id 25 & 

taskset --cpu-list 11 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M26_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32 --id 26 & 

taskset --cpu-list 12 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M27_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32 --id 27 & 

taskset --cpu-list 13 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M28_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32 --id 28 &

taskset --cpu-list 14 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M29_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32  --id 29 & 

taskset --cpu-list 15 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M30_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32 --id 30 & 

taskset --cpu-list 16 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M31_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset ijcnn1 --Nworkers 32 --id 31 & 



#########################################################
                        phishing
#########################################################

----------------------   4 workers  --------------------------


taskset --cpu-list 5 python3 pom1_NN_master_pycloudmessenger_nonid.py --user UC3Mm_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 4 &

taskset --cpu-list 1 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M0_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 4 --id 0 &

taskset --cpu-list 2 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M1_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 4  --id 1 & 

taskset --cpu-list 3 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M2_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 4 --id 2 & 

taskset --cpu-list 4 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M3_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 4 --id 3 & 

----------------------   8 workers  --------------------------

taskset --cpu-list 9 python3 pom1_NN_master_pycloudmessenger_nonid.py --user UC3Mm_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 8 &

taskset --cpu-list 1 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M0_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 8 --id 0 &

taskset --cpu-list 2 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M1_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 8  --id 1 & 

taskset --cpu-list 3 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M2_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 8 --id 2 & 

taskset --cpu-list 4 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M3_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 8 --id 3 & 

taskset --cpu-list 5 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M4_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 8 --id 4 &

taskset --cpu-list 6 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M5_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 8  --id 5 & 

taskset --cpu-list 7 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M6_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 8 --id 6 & 

taskset --cpu-list 8 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M7_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 8 --id 7 & 

----------------------   16 workers  --------------------------

taskset --cpu-list 17 python3 pom1_NN_master_pycloudmessenger_nonid.py --user UC3Mm_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 16 &

taskset --cpu-list 1 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M0_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 16 --id 0 &

taskset --cpu-list 2 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M1_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 16  --id 1 & 

taskset --cpu-list 3 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M2_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 16 --id 2 & 

taskset --cpu-list 4 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M3_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 16 --id 3 & 

taskset --cpu-list 5 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M4_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 16 --id 4 &

taskset --cpu-list 6 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M5_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 16  --id 5 & 

taskset --cpu-list 7 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M6_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 16 --id 6 & 

taskset --cpu-list 8 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M7_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 16 --id 7 & 

taskset --cpu-list 9 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M8_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 16 --id 8 &

taskset --cpu-list 10 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M9_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 16  --id 9 & 

taskset --cpu-list 11 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M10_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 16 --id 10 & 

taskset --cpu-list 12 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M11_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 16 --id 11 & 

taskset --cpu-list 13 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M12_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 16 --id 12 &

taskset --cpu-list 14 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M13_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 16  --id 13 & 

taskset --cpu-list 15 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M14_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 16 --id 14 & 

taskset --cpu-list 16 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M15_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 16 --id 15 & 

----------------------   32 workers  --------------------------

********   Máquina 1

taskset --cpu-list 17 python3 pom1_NN_master_pycloudmessenger_nonid.py --user UC3Mm_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32 &

taskset --cpu-list 1 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M0_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32 --id 0 &

taskset --cpu-list 2 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M1_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32  --id 1 & 

taskset --cpu-list 3 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M2_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32 --id 2 & 

taskset --cpu-list 4 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M3_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32 --id 3 & 

taskset --cpu-list 5 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M4_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32 --id 4 &

taskset --cpu-list 6 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M5_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32  --id 5 & 

taskset --cpu-list 7 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M6_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32 --id 6 & 

taskset --cpu-list 8 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M7_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32 --id 7 & 

taskset --cpu-list 9 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M8_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32 --id 8 &

taskset --cpu-list 10 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M9_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32  --id 9 & 

taskset --cpu-list 11 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M10_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32 --id 10 & 

taskset --cpu-list 12 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M11_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32 --id 11 & 

taskset --cpu-list 13 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M12_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32 --id 12 &

taskset --cpu-list 14 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M13_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32  --id 13 & 

taskset --cpu-list 15 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M14_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32 --id 14 & 

taskset --cpu-list 16 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M15_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32 --id 15 & 

********   Máquina 2

taskset --cpu-list 1 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M16_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32 --id 16 &

taskset --cpu-list 2 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M17_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32  --id 17 & 

taskset --cpu-list 3 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M18_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32 --id 18 & 

taskset --cpu-list 4 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M19_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32 --id 19 & 

taskset --cpu-list 5 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M20_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32 --id 20 &

taskset --cpu-list 6 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M21_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32  --id 21 & 

taskset --cpu-list 7 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M22_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32 --id 22 & 

taskset --cpu-list 8 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M23_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32 --id 23 & 

taskset --cpu-list 9 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M24_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32 --id 24 &

taskset --cpu-list 10 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M25_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32  --id 25 & 

taskset --cpu-list 11 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M26_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32 --id 26 & 

taskset --cpu-list 12 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M27_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32 --id 27 & 

taskset --cpu-list 13 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M28_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32 --id 28 &

taskset --cpu-list 14 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M29_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32  --id 29 & 

taskset --cpu-list 15 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M30_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32 --id 30 & 

taskset --cpu-list 16 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M31_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset phishing --Nworkers 32 --id 31 & 


#########################################################
                        income
#########################################################

----------------------   4 workers  --------------------------


taskset --cpu-list 5 python3 pom1_NN_master_pycloudmessenger_nonid.py --user UC3Mm_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 4 &

taskset --cpu-list 1 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M0_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 4 --id 0 &

taskset --cpu-list 2 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M1_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 4  --id 1 & 

taskset --cpu-list 3 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M2_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 4 --id 2 & 

taskset --cpu-list 4 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M3_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 4 --id 3 & 

----------------------   8 workers  --------------------------

taskset --cpu-list 9 python3 pom1_NN_master_pycloudmessenger_nonid.py --user UC3Mm_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 8 &

taskset --cpu-list 1 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M0_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 8 --id 0 &

taskset --cpu-list 2 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M1_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 8  --id 1 & 

taskset --cpu-list 3 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M2_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 8 --id 2 & 

taskset --cpu-list 4 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M3_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 8 --id 3 & 

taskset --cpu-list 5 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M4_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 8 --id 4 &

taskset --cpu-list 6 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M5_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 8  --id 5 & 

taskset --cpu-list 7 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M6_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 8 --id 6 & 

taskset --cpu-list 8 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M7_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 8 --id 7 & 

----------------------   16 workers  --------------------------

taskset --cpu-list 17 python3 pom1_NN_master_pycloudmessenger_nonid.py --user UC3Mm_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 16 &

taskset --cpu-list 1 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M0_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 16 --id 0 &

taskset --cpu-list 2 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M1_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 16  --id 1 & 

taskset --cpu-list 3 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M2_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 16 --id 2 & 

taskset --cpu-list 4 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M3_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 16 --id 3 & 

taskset --cpu-list 5 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M4_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 16 --id 4 &

taskset --cpu-list 6 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M5_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 16  --id 5 & 

taskset --cpu-list 7 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M6_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 16 --id 6 & 

taskset --cpu-list 8 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M7_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 16 --id 7 & 

taskset --cpu-list 9 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M8_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 16 --id 8 &

taskset --cpu-list 10 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M9_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 16  --id 9 & 

taskset --cpu-list 11 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M10_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 16 --id 10 & 

taskset --cpu-list 12 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M11_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 16 --id 11 & 

taskset --cpu-list 13 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M12_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 16 --id 12 &

taskset --cpu-list 14 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M13_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 16  --id 13 & 

taskset --cpu-list 15 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M14_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 16 --id 14 & 

taskset --cpu-list 16 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M15_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 16 --id 15 & 

----------------------   32 workers  --------------------------

********   Máquina 1

taskset --cpu-list 17 python3 pom1_NN_master_pycloudmessenger_nonid.py --user UC3Mm_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32 &

taskset --cpu-list 1 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M0_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32 --id 0 &

taskset --cpu-list 2 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M1_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32  --id 1 & 

taskset --cpu-list 3 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M2_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32 --id 2 & 

taskset --cpu-list 4 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M3_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32 --id 3 & 

taskset --cpu-list 5 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M4_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32 --id 4 &

taskset --cpu-list 6 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M5_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32  --id 5 & 

taskset --cpu-list 7 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M6_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32 --id 6 & 

taskset --cpu-list 8 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M7_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32 --id 7 & 

taskset --cpu-list 9 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M8_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32 --id 8 &

taskset --cpu-list 10 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M9_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32  --id 9 & 

taskset --cpu-list 11 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M10_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32 --id 10 & 

taskset --cpu-list 12 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M11_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32 --id 11 & 

taskset --cpu-list 13 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M12_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32 --id 12 &

taskset --cpu-list 14 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M13_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32  --id 13 & 

taskset --cpu-list 15 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M14_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32 --id 14 & 

taskset --cpu-list 16 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M15_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32 --id 15 & 

********   Máquina 2

taskset --cpu-list 1 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M16_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32 --id 16 &

taskset --cpu-list 2 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M17_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32  --id 17 & 

taskset --cpu-list 3 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M18_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32 --id 18 & 

taskset --cpu-list 4 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M19_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32 --id 19 & 

taskset --cpu-list 5 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M20_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32 --id 20 &

taskset --cpu-list 6 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M21_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32  --id 21 & 

taskset --cpu-list 7 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M22_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32 --id 22 & 

taskset --cpu-list 8 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M23_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32 --id 23 & 

taskset --cpu-list 9 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M24_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32 --id 24 &

taskset --cpu-list 10 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M25_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32  --id 25 & 

taskset --cpu-list 11 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M26_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32 --id 26 & 

taskset --cpu-list 12 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M27_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32 --id 27 & 

taskset --cpu-list 13 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M28_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32 --id 28 &

taskset --cpu-list 14 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M29_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32  --id 29 & 

taskset --cpu-list 15 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M30_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32 --id 30 & 

taskset --cpu-list 16 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M31_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset income --Nworkers 32 --id 31 & 


#########################################################
                        webspam
#########################################################

----------------------   4 workers  --------------------------


taskset --cpu-list 5 python3 pom1_NN_master_pycloudmessenger_nonid.py --user UC3Mm_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 4 &

taskset --cpu-list 1 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M0_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 4 --id 0 &

taskset --cpu-list 2 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M1_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 4  --id 1 & 

taskset --cpu-list 3 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M2_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 4 --id 2 & 

taskset --cpu-list 4 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M3_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 4 --id 3 & 

----------------------   8 workers  --------------------------

taskset --cpu-list 9 python3 pom1_NN_master_pycloudmessenger_nonid.py --user UC3Mm_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 8 &

taskset --cpu-list 1 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M0_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 8 --id 0 &

taskset --cpu-list 2 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M1_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 8  --id 1 & 

taskset --cpu-list 3 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M2_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 8 --id 2 & 

taskset --cpu-list 4 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M3_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 8 --id 3 & 

taskset --cpu-list 5 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M4_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 8 --id 4 &

taskset --cpu-list 6 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M5_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 8  --id 5 & 

taskset --cpu-list 7 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M6_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 8 --id 6 & 

taskset --cpu-list 8 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M7_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 8 --id 7 & 

----------------------   16 workers  --------------------------

taskset --cpu-list 17 python3 pom1_NN_master_pycloudmessenger_nonid.py --user UC3Mm_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 16 &

taskset --cpu-list 1 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M0_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 16 --id 0 &

taskset --cpu-list 2 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M1_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 16  --id 1 & 

taskset --cpu-list 3 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M2_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 16 --id 2 & 

taskset --cpu-list 4 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M3_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 16 --id 3 & 

taskset --cpu-list 5 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M4_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 16 --id 4 &

taskset --cpu-list 6 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M5_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 16  --id 5 & 

taskset --cpu-list 7 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M6_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 16 --id 6 & 

taskset --cpu-list 8 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M7_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 16 --id 7 & 

taskset --cpu-list 9 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M8_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 16 --id 8 &

taskset --cpu-list 10 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M9_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 16  --id 9 & 

taskset --cpu-list 11 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M10_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 16 --id 10 & 

taskset --cpu-list 12 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M11_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 16 --id 11 & 

taskset --cpu-list 13 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M12_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 16 --id 12 &

taskset --cpu-list 14 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M13_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 16  --id 13 & 

taskset --cpu-list 15 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M14_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 16 --id 14 & 

taskset --cpu-list 16 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M15_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 16 --id 15 & 

----------------------   32 workers  --------------------------

********   Máquina 1

taskset --cpu-list 17 python3 pom1_NN_master_pycloudmessenger_nonid.py --user UC3Mm_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32 &

taskset --cpu-list 1 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M0_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32 --id 0 &

taskset --cpu-list 2 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M1_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32  --id 1 & 

taskset --cpu-list 3 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M2_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32 --id 2 & 

taskset --cpu-list 4 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M3_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32 --id 3 & 

taskset --cpu-list 5 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M4_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32 --id 4 &

taskset --cpu-list 6 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M5_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32  --id 5 & 

taskset --cpu-list 7 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M6_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32 --id 6 & 

taskset --cpu-list 8 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M7_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32 --id 7 & 

taskset --cpu-list 9 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M8_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32 --id 8 &

taskset --cpu-list 10 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M9_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32  --id 9 & 

taskset --cpu-list 11 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M10_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32 --id 10 & 

taskset --cpu-list 12 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M11_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32 --id 11 & 

taskset --cpu-list 13 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M12_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32 --id 12 &

taskset --cpu-list 14 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M13_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32  --id 13 & 

taskset --cpu-list 15 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M14_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32 --id 14 & 

taskset --cpu-list 16 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M15_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32 --id 15 & 

********   Máquina 2

taskset --cpu-list 1 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M16_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32 --id 16 &

taskset --cpu-list 2 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M17_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32  --id 17 & 

taskset --cpu-list 3 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M18_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32 --id 18 & 

taskset --cpu-list 4 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M19_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32 --id 19 & 

taskset --cpu-list 5 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M20_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32 --id 20 &

taskset --cpu-list 6 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M21_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32  --id 21 & 

taskset --cpu-list 7 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M22_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32 --id 22 & 

taskset --cpu-list 8 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M23_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32 --id 23 & 

taskset --cpu-list 9 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M24_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32 --id 24 &

taskset --cpu-list 10 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M25_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32  --id 25 & 

taskset --cpu-list 11 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M26_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32 --id 26 & 

taskset --cpu-list 12 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M27_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32 --id 27 & 

taskset --cpu-list 13 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M28_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32 --id 28 &

taskset --cpu-list 14 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M29_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32  --id 29 & 

taskset --cpu-list 15 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M30_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32 --id 30 & 

taskset --cpu-list 16 python3 pom1_NN_worker_pycloudmessenger_nonid.py --user UC3M31_vasaert6 --password passUC3M --task_name TaskUC3M_vasaert6 --dataset webspam --Nworkers 32 --id 31 & 



