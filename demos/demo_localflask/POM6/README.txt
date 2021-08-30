==================================================================
 Demo execution instructions using localflask under Linux OS
==================================================================

Open 7 bash terminals and activate the environment in everyone of them (conda activate demo), and execute any of the following scripts to see the corresponding demo. 

Every terminal represents one participant, they have to be in the same machine.

-------------------------------------------
Execute these lines, one at every terminal:
-------------------------------------------

python3 local_flask_server.py
python3 pom6_Kmeans_pm_master_localflask.py --dataset synth2D --verbose 1
python3 pom6_Kmeans_pm_worker_localflask.py --id 0 --dataset synth2D --verbose 1
python3 pom6_Kmeans_pm_worker_localflask.py --id 1 --dataset synth2D --verbose 1
python3 pom6_Kmeans_pm_worker_localflask.py --id 2 --dataset synth2D --verbose 1
python3 pom6_Kmeans_pm_worker_localflask.py --id 3 --dataset synth2D --verbose 1
python3 pom6_Kmeans_pm_worker_localflask.py --id 4 --dataset synth2D --verbose 1












python3 local_flask_server.py
python3 pom6_XC_master_localflask.py --dataset redwine --verbose 1
python3 pom6_XC_worker_localflask.py --id 0 --dataset redwine --verbose 1
python3 pom6_XC_worker_localflask.py --id 1 --dataset redwine --verbose 1
python3 pom6_XC_worker_localflask.py --id 2 --dataset redwine --verbose 1
python3 pom6_XC_worker_localflask.py --id 3 --dataset redwine --verbose 1
python3 pom6_XC_worker_localflask.py --id 4 --dataset redwine --verbose 1

python3 local_flask_server.py
python3 pom6_RR_master_localflask.py --dataset redwine --verbose 1
python3 pom6_RR_worker_localflask.py --id 0 --dataset redwine --verbose 1
python3 pom6_RR_worker_localflask.py --id 1 --dataset redwine --verbose 1
python3 pom6_RR_worker_localflask.py --id 2 --dataset redwine --verbose 1
python3 pom6_RR_worker_localflask.py --id 3 --dataset redwine --verbose 1
python3 pom6_RR_worker_localflask.py --id 4 --dataset redwine --verbose 1

python3 local_flask_server.py
python3 pom6_LC_pm_master_localflask.py --dataset pima --verbose 1
python3 pom6_LC_pm_worker_localflask.py --id 0 --dataset pima --verbose 1
python3 pom6_LC_pm_worker_localflask.py --id 1 --dataset pima --verbose 1
python3 pom6_LC_pm_worker_localflask.py --id 2 --dataset pima --verbose 1
python3 pom6_LC_pm_worker_localflask.py --id 3 --dataset pima --verbose 1

python3 local_flask_server.py
python3 pom6_KR_pm_master_localflask.py --dataset sinc1D --verbose 1
python3 pom6_KR_pm_worker_localflask.py --id 0 --dataset sinc1D --verbose 1
python3 pom6_KR_pm_worker_localflask.py --id 1 --dataset sinc1D --verbose 1
python3 pom6_KR_pm_worker_localflask.py --id 2 --dataset sinc1D --verbose 1
python3 pom6_KR_pm_worker_localflask.py --id 3 --dataset sinc1D --verbose 1
python3 pom6_KR_pm_worker_localflask.py --id 4 --dataset sinc1D --verbose 1


pending...

python3 local_flask_server.py
python3 pom6_MLC_pm_master_localflask.py --dataset pima --verbose 1
python3 pom6_MLC_pm_worker_localflask.py --id 0 --dataset pima --verbose 1
python3 pom6_MLC_pm_worker_localflask.py --id 1 --dataset pima --verbose 1
python3 pom6_MLC_pm_worker_localflask.py --id 2 --dataset pima --verbose 1
python3 pom6_MLC_pm_worker_localflask.py --id 3 --dataset pima --verbose 1


python3 local_flask_server.py
python3 pom6_Kmeans_pm_master_localflask.py --dataset synth2D --verbose 1
python3 pom6_Kmeans_pm_worker_localflask.py --id 0 --dataset synth2D --verbose 1
python3 pom6_Kmeans_pm_worker_localflask.py --id 1 --dataset synth2D --verbose 1
python3 pom6_Kmeans_pm_worker_localflask.py --id 2 --dataset synth2D --verbose 1
python3 pom6_Kmeans_pm_worker_localflask.py --id 3 --dataset synth2D --verbose 1
python3 pom6_Kmeans_pm_worker_localflask.py --id 4 --dataset synth2D --verbose 1




FIN






















Terminal 4: 
sh POM6_Kmeans_pm_synth2D_localflask_4workers.sh





# check local_flask

Terminal 0: python3 local_flask_server.py

Terminal 1: 
python3 pom6_Kmeans_pm_master.py --dataset synth2D --verbose 1 --platform localflask

Terminal 2: 
python pom6_Kmeans_pm_worker.py --id 0 --dataset synth2D --verbose 1  --platform localflask

Terminal 3: 
sh POM6_Kmeans_pm_synth2D_localflask_4workers.sh














To run a Kmeans demo on mnist dataset under POM1:
Terminal 1: python3 local_flask_server.py
Terminal 2: sh demo_POM1_Kmeans_mnist.sh

To run a Kmeans demo on mnist dataset under POM2:
Terminal 1: python3 local_flask_server.py
Terminal 2: sh demo_POM2_Kmeans_mnist.sh

To run a Kmeans demo on mnist dataset under POM3:
Terminal 1: python3 local_flask_server.py
Terminal 2: sh demo_POM3_Kmeans_mnist.sh

To run a Logistic Classifier demo on mnist dataset under POM6:
Terminal 1: python3 local_flask_server.py
Terminal 2: sh demo_POM6_LC_mnist.sh


=======================
 FULL DETAIL EXECUTION
=======================

Open 7 bash terminals and activate the environment in everyone of them (conda activate demo). Move to the "demo" folder (cd demo) and execute any of the following scripts to see the corresponding demo: 

---------------------------------------------------------------------------
To run demo POM1 Kmeans mnist, execute these lines, one at every terminal:

Terminal 1: python3 local_flask_server.py
Terminal 2: python3 pom1_Kmeans_worker.py --id 0 --dataset mnist --verbose True
Terminal 3: python3 pom1_Kmeans_worker.py --id 1 --dataset mnist --verbose True
Terminal 4: python3 pom1_Kmeans_worker.py --id 2 --dataset mnist --verbose True
Terminal 5: python3 pom1_Kmeans_worker.py --id 3 --dataset mnist --verbose True
Terminal 6: python3 pom1_Kmeans_worker.py --id 4 --dataset mnist --verbose True
Terminal 7: python3 pom1_Kmeans_master.py --dataset mnist --verbose True

---------------------------------------------------------------------------
To run demo POM2 Kmeans mnist, execute these lines, one at every terminal:

Terminal 1: python3 local_flask_server.py
Terminal 2: python3 pom2_Kmeans_worker.py --id 0 --dataset mnist --verbose True
Terminal 3: python3 pom2_Kmeans_worker.py --id 1 --dataset mnist --verbose True
Terminal 4: python3 pom2_Kmeans_worker.py --id 2 --dataset mnist --verbose True
Terminal 5: python3 pom2_Kmeans_worker.py --id 3 --dataset mnist --verbose True
Terminal 6: python3 pom2_Kmeans_worker.py --id 4 --dataset mnist --verbose True
Terminal 7: python3 pom2_Kmeans_master.py --dataset mnist --verbose True

---------------------------------------------------------------------------
To run demo POM3 Kmeans mnist, execute these lines, one at every terminal:

Terminal 1: python3 local_flask_server.py
Terminal 2: python3 pom3_Kmeans_worker.py --id 0 --dataset mnist --verbose True
Terminal 3: python3 pom3_Kmeans_worker.py --id 1 --dataset mnist --verbose True
Terminal 4: python3 pom3_Kmeans_worker.py --id 2 --dataset mnist --verbose True
Terminal 5: python3 pom3_Kmeans_worker.py --id 3 --dataset mnist --verbose True
Terminal 6: python3 pom3_Kmeans_worker.py --id 4 --dataset mnist --verbose True
Terminal 7: python3 pom3_Kmeans_master.py --dataset mnist --verbose True


---------------------------------------------------------------------------
To run demo POM5 Kmeans synth2D at cloud, execute these lines, one at every terminal:

Terminal 1: python3 pom5_Kmeans_master_cloud.py --dataset synth2D --verbose 1 --platform pycloudmessenger

Terminal 2: python pom5_Kmeans_worker_cloud.py --id 0workerA --dataset synth2D --verbose 1  --platform pycloudmessenger

Terminal 3: sh POM5_Kmeans_synth2D_cloud_4workers.sh


---------------------------------------------------------------------------
To run demo POM6 LC mnist, (local), execute these lines, one at every terminal:

Terminal 1: python3 local_flask_server.py
Terminal 2: python3 pom6_LC_worker.py --id 0 --dataset mnist --verbose True
Terminal 3: python3 pom6_LC_worker.py --id 1 --dataset mnist --verbose True
Terminal 4: python3 pom6_LC_worker.py --id 2 --dataset mnist --verbose True
Terminal 5: python3 pom6_LC_worker.py --id 3 --dataset mnist --verbose True
Terminal 6: python3 pom6_LC_worker.py --id 4 --dataset mnist --verbose True
Terminal 7: python3 pom6_LC_master.py --dataset mnist --verbose True

---------------------------------------------------------------------------
To run demo POM6 LC pima at cloud, execute these lines, one at every terminal:

Terminal 1: python3 pom6_LC_master_cloud.py --dataset pima --verbose 1 --platform pycloudmessenger

Terminal 2: python pom6_LC_worker_cloud.py --id 0workerA --dataset pima --verbose 1  --platform pycloudmessenger

Terminal 3: sh POM6_LC_pima_cloud_4workers.sh


---------------------------------------------------------------------------
To run demo POM6 LC mnist at cloud, execute these lines, one at every terminal:

Terminal 1: python3 pom6_LC_master_cloud.py --dataset mnist --verbose 1 --platform pycloudmessenger

Terminal 2: python pom6_LC_worker_cloud.py --id 0workerA --dataset mnist --verbose 1  --platform pycloudmessenger

Terminal 3: sh POM6_LC_mnist_cloud_4workers.sh


---------------------------------------------------------------------------
To run demo POM6 Kmeans_pm synth2D at cloud, execute these lines, one at every terminal:

Terminal 1: python3 pom6_Kmeans_pm_master_cloud.py --dataset synth2D --verbose 1 --platform pycloudmessenger

Terminal 2: python pom6_Kmeans_pm_worker_cloud.py --id 0workerA --dataset synth2D --verbose 1  --platform pycloudmessenger

Terminal 3: sh POM6_Kmeans_pm_synth2D_cloud_4workers.sh

