==================================================================
 Demo execution instructions using localflask under Linux OS
==================================================================

Open four bash terminals and execute any of the following scripts to see the corresponding demo.

One terminal is used for local communication. Each of the rest represent one participant in the task.

-------------------------------------------
Execute these lines, one at every terminal. Launch the local_flask_server first

Once the training is completed, these demo scripts produce the output files in the results/ folder (models, figures, logs)
-------------------------------------------

Parameters:
    - id: Integer representing the partition of data to be used by the worker. Each worker should use a different partition, possible values are 0 to 4.
    - preprocessing: String indicating wether to apply standard normalization. Any string is valid.

Important notes:
    - Each user should have a different id, otherwise they will be training using the same dataset partition.
-------------------------------------------


==================================================================
 Without normalization and 2 workers
==================================================================
python ../../local_flask_server.py
python pom3_Kmeans_master_local_flask.py
python pom3_Kmeans_worker_local_flask.py --id 0
python pom3_Kmeans_worker_local_flask.py --id 1


==================================================================
 With standard normalization and 2 workers
==================================================================
python ../../local_flask_server.py
python pom3_Kmeans_master_local_flask.py --preprocessing std
python pom3_Kmeans_worker_local_flask.py --id 0
python pom3_Kmeans_worker_local_flask.py --id 1

