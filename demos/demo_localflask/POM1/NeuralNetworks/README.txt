==================================================================
 Demo execution instructions using pycloudmessenger under Linux OS
==================================================================

Open four bash terminals and execute any of the following scripts to see the corresponding demo.

The first terminal is the one for local communications and each of the others represents one participant.

-------------------------------------------
Execute these lines, one at every terminal.

Once the training is completed, these demo scripts produce the output files in the results/ folder (models, figures, logs)
-------------------------------------------

Parameters:
    - id: Integer representing the partition of data to be used by the worker. Each worker should use a different partition, possible values are 0 to 4.

Important notes:
    - Each user should have a different id, otherwise they will be training using the same dataset partition.
    - The architecture of the Keras model to use is defined inside this folder. If you want to try a different architecture use the script model_definition_keras.py and define a new architecture using the sequential or functional API provided by Keras. This new filename should be updated at the beginning of pom1_NN_gradient_averaging_master_pycloudmessenger.py and pom1_NN_model_averaging_master_pycloudmessenger.py in order for the changes to take place.
-------------------------------------------


==================================================================
 Gradient averaging
==================================================================
python ../../local_flask_server.py
python pom1_NN_gradient_averaging_master_local_flask.py
python pom1_NN_worker_local_flask.py --id 0
python pom1_NN_worker_local_flask.py --id 1


==================================================================
 Model averaging
==================================================================
python ../../local_flask_server.py
python pom1_NN_model_averaging_master_local_flask.py
python pom1_NN_worker_local_flask.py --id 0
python pom1_NN_worker_local_flask.py --id 1

