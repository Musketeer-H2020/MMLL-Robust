==================================================================================
Pre-processing, normalization, data alignment estimation and data value estimation
==================================================================================
 Demo execution instructions using pycloudmessenger
==================================================================


==================================================================
 Check data demo with wrong data in worker 1
==================================================================
python pom1_check_data.py --user <user> --password <password> --task_name <task_name> --dataset income_raw
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset income_raw --id 0
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset mnist --id 1


==================================================================
 Data conversion to numeric format demo
==================================================================
python pom1_data_to_numeric.py --user <user> --password <password> --task_name <task_name> --dataset income_raw
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset income_raw --id 0
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset income_raw --id 1


==================================================================
 Data alignment estimation demo
==================================================================
python pom1_data_alignment_estimation.py --user <user> --password <password> --task_name <task_name> --dataset income_raw_bad24
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset income_raw_bad24 --id 0
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset income_raw_bad24 --id 1
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset income_raw_bad24 --id 2
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset income_raw_bad24 --id 3
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset income_raw_bad24 --id 4


==================================================================
 Ad-hoc preprocessing demo
==================================================================
python pom1_adhoc_preprocess.py --user <user> --password <password> --task_name <task_name> --dataset income_raw
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset income_raw --id 0
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset income_raw --id 1


==================================================================
 Image reshape demo
==================================================================
python pom1_image_reshape_preprocessing.py --user <user> --password <password> --task_name <task_name> --dataset mnist_raw_matrix_binclass
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset mnist_raw_matrix_binclass --id 0
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset mnist_raw_matrix_binclass --id 1


==================================================================
 Normalization demo
==================================================================
python pom1_normalization.py --user <user> --password <password> --task_name <task_name> --dataset income_raw
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset income_raw --id 0
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset income_raw --id 1


==================================================================
 Principal component analysis demo
==================================================================
python pom1_principal_component_analysis.py --user <user> --password <password> --task_name <task_name> --dataset income_raw
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset income_raw --id 0
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset income_raw --id 1


==================================================================
 Greedy feature selection demo
==================================================================
python pom1_greedy_feature_selection.py --user <user> --password <password> --task_name <task_name> --dataset income_raw
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset income_raw --id 0
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset income_raw --id 1


==================================================================
 Feature frequency selection demo
==================================================================
python pom1_feature_selection_frequency.py --user <user> --password <password> --task_name <task_name> --dataset news20_all_sparse
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset news20_all_sparse --id 0
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset news20_all_sparse --id 1


==================================================================
 Random projection demo
==================================================================
python pom1_random_projection.py --user <user> --password <password> --task_name <task_name> --dataset news20_all_sparse
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset news20_all_sparse --id 0
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset news20_all_sparse --id 1


==================================================================
 Deep Learning preprocessing demo
==================================================================
python pom1_deep_learning_preprocessing.py --user <user> --password <password> --task_name <task_name> --dataset mnist_raw_matrix_binclass
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset mnist_raw_matrix_binclass --id 0
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset mnist_raw_matrix_binclass --id 1


==================================================================
 Natural language processing (TFIDF) demo
==================================================================
python pom1_natural_language_processing.py --user <user> --password <password> --task_name <task_name> --dataset 20news_bow_bin
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset 20news_bow_bin --id 0
python pom1_worker.py --user <user> --password <password> --task_name <task_name> --dataset 20news_bow_bin --id 1


==================================================================
 Record linkage demo
==================================================================
python pom1_record_linkage.py --user <user> --password <password> --task_name <task_name> --dataset income_raw_V
python pom1_worker_V.py --user <user> --password <password> --task_name <task_name> --dataset income_raw_V --id 0
python pom1_worker_V.py --user <user> --password <password> --task_name <task_name> --dataset income_raw_V --id 1


==================================================================
 Missing data imputation demo
==================================================================
python pom1_missing_data_imputation.py --user <user> --password <password> --task_name <task_name> --dataset income_raw_V_missing
python pom1_worker_V.py --user <user> --password <password> --task_name <task_name> --dataset income_raw_V_missing --id 0
python pom1_worker_V.py --user <user> --password <password> --task_name <task_name> --dataset income_raw_V_missing --id 1
