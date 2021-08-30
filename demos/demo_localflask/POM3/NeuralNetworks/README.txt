==================================================================
 Demo execution instructions using pycloudmessenger under Linux OS
==================================================================

Open four bash terminals and execute any of the following scripts to see the corresponding demo.

One terminal is used for local communication. Each of the rest represent one participant in the task.

-------------------------------------------
Execute these lines, one at every terminal.

Once the training is completed, these demo scripts produce the output files in the results/ folder (models, figures, logs)
-------------------------------------------

Parameters:
    - id: Integer representing the partition of data to be used by the worker. Each worker should use a different partition, possible values are 0 to 4.
    - preprocessing: String indicating whether to apply standard normalization. Any string is valid. By default no normalization is used.
    - implementation: String indicating whether to use gradient_averaging or model_averaging implementation. By default the latter is used. 

Important notes:
    - The local flask server terminal should be run first, otherwise no communication is available and an error is produced.
    - Each user should have a different id, otherwise they will be training using the same dataset partition.
    - The architecture of the Keras model to use is defined inside this folder. If you want to try a different architecture use the script Model_definition_keras.py for defining a new architecture using the sequential or functional API provided by Keras. Afterwards run python Model_definition_keras.py to save the new file. This new filename should be updated at the beginning of pom3_NN_master_pycloudmessenger.py in order for the changes to take place.
-------------------------------------------


==================================================================
 Model averaging
==================================================================
python ../../local_flask_server.py
python pom3_NN_master_local_flask.py
python pom3_NN_worker_local_flask.py --id 0
python pom3_NN_worker_local_flask.py --id 1


==================================================================
 Gradient averaging
==================================================================
python ../../local_flask_server.py
python pom3_NN_master_local_flask.py --implementation gradient_averaging
python pom3_NN_worker_local_flask.py --id 0
python pom3_NN_worker_local_flask.py --id 1


==================================================================
 Model averaging with standard normalization
==================================================================
python ../../local_flask_server.py
python pom3_NN_master_local_flask.py --preprocessing std
python pom3_NN_worker_local_flask.py --id 0
python pom3_NN_worker_local_flask.py --id 1


==================================================================
 Gradient averaging with standard normalization
==================================================================
python ../../local_flask_server.py
python pom3_NN_master_local_flask.py --implementation gradient_averaging --preprocessing std
python pom3_NN_worker_local_flask.py --id 0
python pom3_NN_worker_local_flask.py --id 1

