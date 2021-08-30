==================================================================
 Demo execution instructions using pycloudmessenger under Linux OS
==================================================================

Open four bash terminals and execute any of the following scripts to see the corresponding demo.

The first terminal is the one for local communication. Each of the rest represent one participant in the task.

-------------------------------------------
Execute these lines, one at every terminal.

Once the training is completed, these demo scripts produce the output files in the results/ folder (models, figures, logs)
-------------------------------------------

Parameters:
    - id: Integer representing the partition of data to be used by the worker. Each worker should use a different partition, possible values are 0 to 4.
-------------------------------------------

python ../../local_flask_server.py
python pom2_Kmeans_master_local_flask.py
python pom2_Kmeans_worker_local_flask.py --id 0
python pom2_Kmeans_worker_local_flask.py --id 1

