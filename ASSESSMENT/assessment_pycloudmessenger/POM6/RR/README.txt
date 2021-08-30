=======================================================================0
1 worker, redwine
=======================================================================0

\rm mprofile_*.dat; mprof run taskset --cpu-list 20 python3 pom6_RR_master_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 1

mprof run taskset --cpu-list 1 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 1 --id 0 


=======================================================================0
5 workers, redwine
=======================================================================0

\rm mprofile_*.dat; mprof run taskset --cpu-list 20 python3 pom6_RR_master_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 5  

mprof run taskset --cpu-list 1 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 5 --id 0  &

sleep 5; mprof run taskset --cpu-list 2 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 5 --id 1 &

sleep 10; mprof run taskset --cpu-list 3 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 5 --id 2 &

sleep 15; mprof run taskset --cpu-list 4 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 5 --id 3 &

sleep 20; mprof run taskset --cpu-list 5 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 5 --id 4 &


=======================================================================0
10 workers, redwine
=======================================================================0

\rm mprofile_*.dat; mprof run taskset --cpu-list 20 python3 pom6_RR_master_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 10 


mprof run taskset --cpu-list 1 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 10 --id 0 &

sleep 5; mprof run taskset --cpu-list 2 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 10 --id 1 &

sleep 10; mprof run taskset --cpu-list 3 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 10 --id 2 &

sleep 15; mprof run taskset --cpu-list 4 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 10 --id 3 &

sleep 20; mprof run taskset --cpu-list 5 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 10 --id 4 &

sleep 25; mprof run taskset --cpu-list 6 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 10 --id 5 &

sleep 30; mprof run taskset --cpu-list 7 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 10 --id 6 &

sleep 35; mprof run taskset --cpu-list 8 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 10 --id 7 &

sleep 40; mprof run taskset --cpu-list 9 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 10 --id 8 &

sleep 45; mprof run taskset --cpu-list 10 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 10 --id 9 &


=======================================================================0
15 workers, redwine
=======================================================================0

\rm mprofile_*.dat; mprof run taskset --cpu-list 20 python3 pom6_RR_master_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 15 


mprof run taskset --cpu-list 1 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 15 --id 0 &

sleep 5; mprof run taskset --cpu-list 2 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 15 --id 1 &

sleep 10; mprof run taskset --cpu-list 3 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 15 --id 2 &

sleep 15; mprof run taskset --cpu-list 4 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 15 --id 3 &

sleep 20; mprof run taskset --cpu-list 5 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 15 --id 4 &

sleep 25; mprof run taskset --cpu-list 6 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 15 --id 5 &

sleep 30; mprof run taskset --cpu-list 7 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 15 --id 6 &

sleep 35; mprof run taskset --cpu-list 8 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 15 --id 7 &

sleep 40; mprof run taskset --cpu-list 9 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 15 --id 8 &

sleep 45; mprof run taskset --cpu-list 10 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 15 --id 9 &

sleep 50; mprof run taskset --cpu-list 11 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 15 --id 10 &

sleep 55; mprof run taskset --cpu-list 12 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 15 --id 11 &

sleep 60; mprof run taskset --cpu-list 13 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 15 --id 12 &

sleep 65; mprof run taskset --cpu-list 14 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 15 --id 13 &

sleep 70; mprof run taskset --cpu-list 15 python3 pom6_RR_worker_pycloudmessenger.py --dataset redwine --verbose 1 --Nworkers 15 --id 14 &









=======================================================================0
1 worker, superconduct_norm
=======================================================================0

\rm mprofile_*.dat; mprof run taskset --cpu-list 20 python3 pom6_RR_master_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 1

mprof run taskset --cpu-list 1 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 1 --id 0 


=======================================================================0
5 workers, superconduct_norm
=======================================================================0

\rm mprofile_*.dat; mprof run taskset --cpu-list 20 python3 pom6_RR_master_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 5  

mprof run taskset --cpu-list 1 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 5 --id 0  &

sleep 5; mprof run taskset --cpu-list 2 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 5 --id 1 &

sleep 10; mprof run taskset --cpu-list 3 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 5 --id 2 &

sleep 15; mprof run taskset --cpu-list 4 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 5 --id 3 &

sleep 20; mprof run taskset --cpu-list 5 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 5 --id 4 &


=======================================================================0
10 workers, superconduct_norm
=======================================================================0

\rm mprofile_*.dat; mprof run taskset --cpu-list 20 python3 pom6_RR_master_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 10 


mprof run taskset --cpu-list 1 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 10 --id 0 &

sleep 5; mprof run taskset --cpu-list 2 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 10 --id 1 &

sleep 10; mprof run taskset --cpu-list 3 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 10 --id 2 &

sleep 15; mprof run taskset --cpu-list 4 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 10 --id 3 &

sleep 20; mprof run taskset --cpu-list 5 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 10 --id 4 &

sleep 25; mprof run taskset --cpu-list 6 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 10 --id 5 &

sleep 30; mprof run taskset --cpu-list 7 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 10 --id 6 &

sleep 35; mprof run taskset --cpu-list 8 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 10 --id 7 &

sleep 40; mprof run taskset --cpu-list 9 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 10 --id 8 &

sleep 45; mprof run taskset --cpu-list 10 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 10 --id 9 &


=======================================================================0
15 workers, superconduct_norm
=======================================================================0

\rm mprofile_*.dat; mprof run taskset --cpu-list 20 python3 pom6_RR_master_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 15 


mprof run taskset --cpu-list 1 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 15 --id 0 &

sleep 5; mprof run taskset --cpu-list 2 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 15 --id 1 &

sleep 10; mprof run taskset --cpu-list 3 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 15 --id 2 &

sleep 15; mprof run taskset --cpu-list 4 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 15 --id 3 &

sleep 20; mprof run taskset --cpu-list 5 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 15 --id 4 &

sleep 25; mprof run taskset --cpu-list 6 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 15 --id 5 &

sleep 30; mprof run taskset --cpu-list 7 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 15 --id 6 &

sleep 35; mprof run taskset --cpu-list 8 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 15 --id 7 &

sleep 40; mprof run taskset --cpu-list 9 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 15 --id 8 &

sleep 45; mprof run taskset --cpu-list 10 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 15 --id 9 &

sleep 50; mprof run taskset --cpu-list 11 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 15 --id 10 &

sleep 55; mprof run taskset --cpu-list 12 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 15 --id 11 &

sleep 60; mprof run taskset --cpu-list 13 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 15 --id 12 &

sleep 65; mprof run taskset --cpu-list 14 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 15 --id 13 &

sleep 70; mprof run taskset --cpu-list 15 python3 pom6_RR_worker_pycloudmessenger.py --dataset superconduct_norm --verbose 1 --Nworkers 15 --id 14 &









=======================================================================0
1 worker, blogfeedback_norm
=======================================================================0

\rm mprofile_*.dat; mprof run taskset --cpu-list 20 python3 pom6_RR_master_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 1

mprof run taskset --cpu-list 1 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 1 --id 0 


=======================================================================0
5 workers, blogfeedback_norm
=======================================================================0

\rm mprofile_*.dat; mprof run taskset --cpu-list 20 python3 pom6_RR_master_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 5  

mprof run taskset --cpu-list 1 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 5 --id 0  &

sleep 5; mprof run taskset --cpu-list 2 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 5 --id 1 &

sleep 10; mprof run taskset --cpu-list 3 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 5 --id 2 &

sleep 15; mprof run taskset --cpu-list 4 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 5 --id 3 &

sleep 20; mprof run taskset --cpu-list 5 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 5 --id 4 &


=======================================================================0
10 workers, blogfeedback_norm
=======================================================================0

\rm mprofile_*.dat; mprof run taskset --cpu-list 20 python3 pom6_RR_master_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 10 


mprof run taskset --cpu-list 1 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 10 --id 0 &

sleep 5; mprof run taskset --cpu-list 2 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 10 --id 1 &

sleep 10; mprof run taskset --cpu-list 3 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 10 --id 2 &

sleep 15; mprof run taskset --cpu-list 4 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 10 --id 3 &

sleep 20; mprof run taskset --cpu-list 5 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 10 --id 4 &

sleep 25; mprof run taskset --cpu-list 6 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 10 --id 5 &

sleep 30; mprof run taskset --cpu-list 7 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 10 --id 6 &

sleep 35; mprof run taskset --cpu-list 8 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 10 --id 7 &

sleep 40; mprof run taskset --cpu-list 9 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 10 --id 8 &

sleep 45; mprof run taskset --cpu-list 10 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 10 --id 9 &


=======================================================================0
15 workers, blogfeedback_norm
=======================================================================0

\rm mprofile_*.dat; mprof run taskset --cpu-list 20 python3 pom6_RR_master_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 15 


mprof run taskset --cpu-list 1 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 15 --id 0 &

sleep 5; mprof run taskset --cpu-list 2 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 15 --id 1 &

sleep 10; mprof run taskset --cpu-list 3 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 15 --id 2 &

sleep 15; mprof run taskset --cpu-list 4 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 15 --id 3 &

sleep 20; mprof run taskset --cpu-list 5 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 15 --id 4 &

sleep 25; mprof run taskset --cpu-list 6 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 15 --id 5 &

sleep 30; mprof run taskset --cpu-list 7 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 15 --id 6 &

sleep 35; mprof run taskset --cpu-list 8 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 15 --id 7 &

sleep 40; mprof run taskset --cpu-list 9 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 15 --id 8 &

sleep 45; mprof run taskset --cpu-list 10 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 15 --id 9 &

sleep 50; mprof run taskset --cpu-list 11 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 15 --id 10 &

sleep 55; mprof run taskset --cpu-list 12 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 15 --id 11 &

sleep 60; mprof run taskset --cpu-list 13 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 15 --id 12 &

sleep 65; mprof run taskset --cpu-list 14 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 15 --id 13 &

sleep 70; mprof run taskset --cpu-list 15 python3 pom6_RR_worker_pycloudmessenger.py --dataset blogfeedback_norm --verbose 1 --Nworkers 15 --id 14 &
