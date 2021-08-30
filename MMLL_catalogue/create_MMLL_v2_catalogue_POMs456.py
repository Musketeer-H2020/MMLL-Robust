# -*- coding: utf-8 -*-

'''
python3 create_MMLL_v2_catalogue_POMs456.py


The catalogue is a list of dicts

dict keys: 

id
POM
type: classification
name: NN
label: ANN (Artificial Neural Network)
description: Generic machine learning algorithm based on neural networks.
properties: list of dicts of properties:
{'name': 'Nmaxiter', 'label': 'Max number of iterations', 'defaultValue': 100, 'type': 'number', 'description': 'Number of epochs.'}

'''

import json
cat = []

#########################################################################
####################   POM 1   ##########################################
#########################################################################



#########################################################################
####################   POM 2   ##########################################
#########################################################################


#########################################################################
####################   POM 3   ##########################################
#########################################################################



#########################################################################
####################   POM 4   ##########################################
#########################################################################

#########################################################################
new_model_dict = {}
new_model_dict.update({'id': 14})
new_model_dict.update({'POM': 4})
new_model_dict.update({'type': 'regression'})
new_model_dict.update({'name': 'LR'})
new_model_dict.update({'label': 'Linear Regression'})
new_model_dict.update({'description': 'Linear Regression model'})
props = []
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'Nmaxiter'})
props_dict.update({'label': 'Max number of iterations.'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Max number of epochs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'conv_stop'})
props_dict.update({'label': 'Convergence threshold'})
props_dict.update({'defaultValue': 0.005})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Convergence value to stop training.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'mu'})
props_dict.update({'label': 'Learning rate'})
props_dict.update({'defaultValue': 0.1})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Learning rate value to update model using gradient descent.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'input_data_description'})
props_dict.update({'label': 'Input data description'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'dictionary'})
props_dict.update({'description': 'Description of the input features.'})
props.append(props_dict)
#---------------------------------------------------
new_model_dict.update({'properties': props})
cat.append(new_model_dict)
#########################################################################


#########################################################################
new_model_dict = {}
new_model_dict.update({'id': 15})
new_model_dict.update({'POM': 4})
new_model_dict.update({'type': 'classifier'})
new_model_dict.update({'name': 'LC'})
new_model_dict.update({'label': 'Logistic Classifier'})
new_model_dict.update({'description': 'Logistic Classifier model'})
props = []
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'Nmaxiter'})
props_dict.update({'label': 'Max number of iterations.'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Max number of epochs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'conv_stop'})
props_dict.update({'label': 'Convergence threshold'})
props_dict.update({'defaultValue': 0.005})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Convergence value to stop training.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'mu'})
props_dict.update({'label': 'Learning rate'})
props_dict.update({'defaultValue': 0.1})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Learning rate value to update model using gradient descent.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'input_data_description'})
props_dict.update({'label': 'Input data description'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'dictionary'})
props_dict.update({'description': 'Description of the input features.'})
props.append(props_dict)
#---------------------------------------------------
new_model_dict.update({'properties': props})
cat.append(new_model_dict)
#########################################################################


#########################################################################
new_model_dict = {}
new_model_dict.update({'id': 16})
new_model_dict.update({'POM': 4})
new_model_dict.update({'type': 'classifier'})
new_model_dict.update({'name': 'MLC'})
new_model_dict.update({'label': 'Multiclass Logistic Classifier'})
new_model_dict.update({'description': 'Multiclass Logistic Classifier model'})
props = []
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'Nmaxiter'})
props_dict.update({'label': 'Max number of iterations.'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Max number of epochs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'conv_stop'})
props_dict.update({'label': 'Convergence threshold'})
props_dict.update({'defaultValue': 0.005})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Convergence value to stop training.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'mu'})
props_dict.update({'label': 'Learning rate'})
props_dict.update({'defaultValue': 0.1})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Learning rate value to update model using gradient descent.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'input_data_description'})
props_dict.update({'label': 'Input data description'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'dictionary'})
props_dict.update({'description': 'Description of the input features.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'target_data_description'})
props_dict.update({'label': 'Target data description'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'dictionary'})
props_dict.update({'description': 'Description of the target values.'})
props.append(props_dict)
#---------------------------------------------------
new_model_dict.update({'properties': props})
cat.append(new_model_dict)
#########################################################################



#########################################################################
new_model_dict = {}
new_model_dict.update({'id': 17})
new_model_dict.update({'POM': 4})
new_model_dict.update({'type': 'clustering'})
new_model_dict.update({'name': 'Kmeans'})
new_model_dict.update({'label': 'Kmeans clustering'})
new_model_dict.update({'description': 'Kmeans clustering algorithm.'})
props = []
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'Nmaxiter'})
props_dict.update({'label': 'Max number of iterations.'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Max number of epochs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'NC'})
props_dict.update({'label': 'Number of centroids'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Number of centroids'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'conv_stop'})
props_dict.update({'label': 'Convergence threshold to stop training.'})
props_dict.update({'defaultValue': 0.005})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Convergence threshold to stop training.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'input_data_description'})
props_dict.update({'label': 'Input data description'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'dictionary'})
props_dict.update({'description': 'Description of the input features.'})
props.append(props_dict)
#---------------------------------------------------
new_model_dict.update({'properties': props})
cat.append(new_model_dict)
#########################################################################


#########################################################################
new_model_dict = {}
new_model_dict.update({'id': 18})
new_model_dict.update({'POM': 4})
new_model_dict.update({'type': 'regression'})
new_model_dict.update({'name': 'KR'})
new_model_dict.update({'label': 'Kernel Regression'})
new_model_dict.update({'description': 'Kernel Regression model using Gaussian kernels.'})
props = []
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'Nmaxiter'})
props_dict.update({'label': 'Max number of iterations.'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Max number of epochs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'conv_stop'})
props_dict.update({'label': 'Convergence threshold'})
props_dict.update({'defaultValue': 0.005})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Convergence value to stop training.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'mu'})
props_dict.update({'label': 'Learning rate'})
props_dict.update({'defaultValue': 0.1})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Learning rate value to update model using gradient descent.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'input_data_description'})
props_dict.update({'label': 'Input data description'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'dictionary'})
props_dict.update({'description': 'Description of the input features.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'fsigma'})
props_dict.update({'label': 'Sigma factor.'})
props_dict.update({'defaultValue': 0.1})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Factor to obtain the sigma value as fsigma * sqrt(NI), where NI is the number of inputs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'C'})
props_dict.update({'label': 'Centroids.'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'matrix'})
props_dict.update({'description': 'Centroids to be used for the computation of the kernels.'})
props.append(props_dict)
#---------------------------------------------------
new_model_dict.update({'properties': props})
cat.append(new_model_dict)
#########################################################################


#########################################################################
new_model_dict = {}
new_model_dict.update({'id': 19})
new_model_dict.update({'POM': 4})
new_model_dict.update({'type': 'classification'})
new_model_dict.update({'name': 'BSVM'})
new_model_dict.update({'label': 'Budget Support Vector Machine'})
new_model_dict.update({'description': 'Support Vector Machine model with controlled complexity (budget) using Gaussian kernels.'})
props = []
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'Nmaxiter'})
props_dict.update({'label': 'Max number of iterations.'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Max number of epochs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'mu'})
props_dict.update({'label': 'Learning rate'})
props_dict.update({'defaultValue': 0.1})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Learning rate value to update model using gradient descent.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'conv_stop'})
props_dict.update({'label': 'Convergence threshold'})
props_dict.update({'defaultValue': 0.005})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Convergence value to stop training.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'Csvm'})
props_dict.update({'label': 'Error penalty'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Penalization of every nonzero slack variable.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'input_data_description'})
props_dict.update({'label': 'Input data description'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'dictionary'})
props_dict.update({'description': 'Description of the input features.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'fsigma'})
props_dict.update({'label': 'Sigma factor.'})
props_dict.update({'defaultValue': 0.1})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Factor to obtain the sigma value as fsigma * sqrt(NI), where NI is the number of inputs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'C'})
props_dict.update({'label': 'Centroids.'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'matrix'})
props_dict.update({'description': 'Centroids to be used for the computation of the kernels, row-wise stored to build a NCxNI matrix.'})
props.append(props_dict)
#---------------------------------------------------
new_model_dict.update({'properties': props})
cat.append(new_model_dict)
#########################################################################

#########################################################################
####################   POM 5   ##########################################
#########################################################################

#########################################################################
new_model_dict = {}
new_model_dict.update({'id': 20})
new_model_dict.update({'POM': 5})
new_model_dict.update({'type': 'regression'})
new_model_dict.update({'name': 'LR'})
new_model_dict.update({'label': 'Linear Regression'})
new_model_dict.update({'description': 'Linear Regression model'})
props = []
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'Nmaxiter'})
props_dict.update({'label': 'Max number of iterations.'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Max number of epochs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'conv_stop'})
props_dict.update({'label': 'Convergence threshold'})
props_dict.update({'defaultValue': 0.005})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Convergence value to stop training.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'mu'})
props_dict.update({'label': 'Learning rate'})
props_dict.update({'defaultValue': 0.1})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Learning rate value to update model using gradient descent.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'input_data_description'})
props_dict.update({'label': 'Input data description'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'dictionary'})
props_dict.update({'description': 'Description of the input features.'})
props.append(props_dict)
#---------------------------------------------------
new_model_dict.update({'properties': props})
cat.append(new_model_dict)
#########################################################################


#########################################################################
new_model_dict = {}
new_model_dict.update({'id': 21})
new_model_dict.update({'POM': 5})
new_model_dict.update({'type': 'classifier'})
new_model_dict.update({'name': 'LC'})
new_model_dict.update({'label': 'Logistic Classifier'})
new_model_dict.update({'description': 'Logistic Classifier model'})
props = []
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'Nmaxiter'})
props_dict.update({'label': 'Max number of iterations.'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Max number of epochs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'conv_stop'})
props_dict.update({'label': 'Convergence threshold'})
props_dict.update({'defaultValue': 0.005})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Convergence value to stop training.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'mu'})
props_dict.update({'label': 'Learning rate'})
props_dict.update({'defaultValue': 0.1})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Learning rate value to update model using gradient descent.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'input_data_description'})
props_dict.update({'label': 'Input data description'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'dictionary'})
props_dict.update({'description': 'Description of the input features.'})
props.append(props_dict)
#---------------------------------------------------
new_model_dict.update({'properties': props})
cat.append(new_model_dict)
#########################################################################

#########################################################################
new_model_dict = {}
new_model_dict.update({'id': 22})
new_model_dict.update({'POM': 5})
new_model_dict.update({'type': 'classifier'})
new_model_dict.update({'name': 'MLC'})
new_model_dict.update({'label': 'Multiclass Logistic Classifier'})
new_model_dict.update({'description': 'Multiclass Logistic Classifier model'})
props = []
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'Nmaxiter'})
props_dict.update({'label': 'Max number of iterations.'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Max number of epochs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'conv_stop'})
props_dict.update({'label': 'Convergence threshold'})
props_dict.update({'defaultValue': 0.005})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Convergence value to stop training.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'mu'})
props_dict.update({'label': 'Learning rate'})
props_dict.update({'defaultValue': 0.1})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Learning rate value to update model using gradient descent.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'input_data_description'})
props_dict.update({'label': 'Input data description'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'dictionary'})
props_dict.update({'description': 'Description of the input features.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'target_data_description'})
props_dict.update({'label': 'Target data description'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'dictionary'})
props_dict.update({'description': 'Description of the target values.'})
props.append(props_dict)
#---------------------------------------------------
new_model_dict.update({'properties': props})
cat.append(new_model_dict)
#########################################################################

#########################################################################
new_model_dict = {}
new_model_dict.update({'id': 23})
new_model_dict.update({'POM': 5})
new_model_dict.update({'type': 'clustering'})
new_model_dict.update({'name': 'Kmeans'})
new_model_dict.update({'label': 'Kmeans clustering'})
new_model_dict.update({'description': 'Kmeans clustering algorithm.'})
props = []
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'Nmaxiter'})
props_dict.update({'label': 'Max number of iterations.'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Max number of epochs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'NC'})
props_dict.update({'label': 'Number of centroids'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Number of centroids'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'conv_stop'})
props_dict.update({'label': 'Convergence threshold to stop training.'})
props_dict.update({'defaultValue': 0.005})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Convergence threshold to stop training.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'input_data_description'})
props_dict.update({'label': 'Input data description'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'dictionary'})
props_dict.update({'description': 'Description of the input features.'})
props.append(props_dict)
#---------------------------------------------------
new_model_dict.update({'properties': props})
cat.append(new_model_dict)
#########################################################################


#########################################################################
new_model_dict = {}
new_model_dict.update({'id': 24})
new_model_dict.update({'POM': 5})
new_model_dict.update({'type': 'regression'})
new_model_dict.update({'name': 'KR'})
new_model_dict.update({'label': 'Kernel Regression'})
new_model_dict.update({'description': 'Kernel Regression model using Gaussian kernels.'})
props = []
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'Nmaxiter'})
props_dict.update({'label': 'Max number of iterations.'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Max number of epochs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'conv_stop'})
props_dict.update({'label': 'Convergence threshold'})
props_dict.update({'defaultValue': 0.005})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Convergence value to stop training.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'mu'})
props_dict.update({'label': 'Learning rate'})
props_dict.update({'defaultValue': 0.1})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Learning rate value to update model using gradient descent.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'input_data_description'})
props_dict.update({'label': 'Input data description'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'dictionary'})
props_dict.update({'description': 'Description of the input features.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'fsigma'})
props_dict.update({'label': 'Sigma factor.'})
props_dict.update({'defaultValue': 0.1})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Factor to obtain the sigma value as fsigma * sqrt(NI), where NI is the number of inputs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'C'})
props_dict.update({'label': 'Centroids.'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'matrix'})
props_dict.update({'description': 'Centroids to be used for the computation of the kernels, row-wise stored to build a NCxNI matrix.'})
props.append(props_dict)
#---------------------------------------------------
new_model_dict.update({'properties': props})
cat.append(new_model_dict)
#########################################################################


#########################################################################
new_model_dict = {}
new_model_dict.update({'id': 25})
new_model_dict.update({'POM': 5})
new_model_dict.update({'type': 'classification'})
new_model_dict.update({'name': 'BSVM'})
new_model_dict.update({'label': 'Budget Support Vector Machine'})
new_model_dict.update({'description': 'Support Vector Machine model with controlled complexity (budget) using Gaussian kernels.'})
props = []
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'Nmaxiter'})
props_dict.update({'label': 'Max number of iterations.'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Max number of epochs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'conv_stop'})
props_dict.update({'label': 'Convergence threshold'})
props_dict.update({'defaultValue': 0.005})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Convergence value to stop training.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'Csvm'})
props_dict.update({'label': 'Error penalty'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Penalization of every nonzero slack variable.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'input_data_description'})
props_dict.update({'label': 'Input data description'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'dictionary'})
props_dict.update({'description': 'Description of the input features.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'fsigma'})
props_dict.update({'label': 'Sigma factor.'})
props_dict.update({'defaultValue': 0.1})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Factor to obtain the sigma value as fsigma * sqrt(NI), where NI is the number of inputs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'C'})
props_dict.update({'label': 'Centroids.'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'matrix'})
props_dict.update({'description': 'Centroids to be used for the computation of the kernels, row-wise stored to build a NCxNI matrix.'})
props.append(props_dict)
#---------------------------------------------------
new_model_dict.update({'properties': props})
cat.append(new_model_dict)
#########################################################################

#########################################################################
new_model_dict = {}
new_model_dict.update({'id': 26})
new_model_dict.update({'POM': 5})
new_model_dict.update({'type': 'classification'})
new_model_dict.update({'name': 'MBSVM'})
new_model_dict.update({'label': 'Multiclass Budget Support Vector Machine'})
new_model_dict.update({'description': 'Support Vector Machine model with controlled complexity (budget) using Gaussian kernels.'})
props = []
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'Nmaxiter'})
props_dict.update({'label': 'Max number of iterations.'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Max number of epochs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'conv_stop'})
props_dict.update({'label': 'Convergence threshold'})
props_dict.update({'defaultValue': 0.005})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Convergence value to stop training.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'Csvm'})
props_dict.update({'label': 'Error penalty'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Penalization of every nonzero slack variable.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'input_data_description'})
props_dict.update({'label': 'Input data description'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'dictionary'})
props_dict.update({'description': 'Description of the input features.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'target_data_description'})
props_dict.update({'label': 'Target data description'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'dictionary'})
props_dict.update({'description': 'Description of the targets.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'fsigma'})
props_dict.update({'label': 'Sigma factor.'})
props_dict.update({'defaultValue': 0.1})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Factor to obtain the sigma value as fsigma * sqrt(NI), where NI is the number of inputs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'C'})
props_dict.update({'label': 'Centroids.'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'matrix'})
props_dict.update({'description': 'Centroids to be used for the computation of the kernels, row-wise stored to build a NCxNI matrix.'})
props.append(props_dict)
#---------------------------------------------------
new_model_dict.update({'properties': props})
cat.append(new_model_dict)
#########################################################################

#########################################################################
####################   POM 6   ##########################################
#########################################################################


#########################################################################
new_model_dict = {}
new_model_dict.update({'id': 27})
new_model_dict.update({'POM': 6})
new_model_dict.update({'type': 'regression'})
new_model_dict.update({'name': 'RR'})
new_model_dict.update({'label': 'Ridge Regression'})
new_model_dict.update({'description': 'Ridge Regression model'})
props = []
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'input_data_description'})
props_dict.update({'label': 'Input data description'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'dictionary'})
props_dict.update({'description': 'Description of the input features.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'regularization'})
props_dict.update({'label': 'Regularization.'})
props_dict.update({'defaultValue': 0.1})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Ridge regularization value used to smooth the model.'})
props.append(props_dict)
#---------------------------------------------------
new_model_dict.update({'properties': props})
cat.append(new_model_dict)
#########################################################################



#########################################################################
new_model_dict = {}
new_model_dict.update({'id': 28})
new_model_dict.update({'POM': 6})
new_model_dict.update({'type': 'classifier'})
new_model_dict.update({'name': 'LC'})
new_model_dict.update({'label': 'Logistic Classifier'})
new_model_dict.update({'description': 'Logistic Classifier model'})
props = []
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'Nmaxiter'})
props_dict.update({'label': 'Max number of iterations.'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Max number of epochs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'conv_stop'})
props_dict.update({'label': 'Convergence threshold'})
props_dict.update({'defaultValue': 0.005})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Convergence value to stop training.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'mu'})
props_dict.update({'label': 'Learning rate'})
props_dict.update({'defaultValue': 0.1})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Learning rate value to update model using gradient descent.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'input_data_description'})
props_dict.update({'label': 'Input data description'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'dictionary'})
props_dict.update({'description': 'Description of the input features.'})
props.append(props_dict)
#---------------------------------------------------
new_model_dict.update({'properties': props})
cat.append(new_model_dict)
#########################################################################

#########################################################################
new_model_dict = {}
new_model_dict.update({'id': 29})
new_model_dict.update({'POM': 6})
new_model_dict.update({'type': 'classifier'})
new_model_dict.update({'name': 'MLC'})
new_model_dict.update({'label': 'Multiclass Logistic Classifier'})
new_model_dict.update({'description': 'Multiclass Logistic Classifier model'})
props = []
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'Nmaxiter'})
props_dict.update({'label': 'Max number of iterations.'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Max number of epochs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'conv_stop'})
props_dict.update({'label': 'Convergence threshold'})
props_dict.update({'defaultValue': 0.005})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Convergence value to stop training.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'mu'})
props_dict.update({'label': 'Learning rate'})
props_dict.update({'defaultValue': 0.1})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Learning rate value to update model using gradient descent.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'input_data_description'})
props_dict.update({'label': 'Input data description'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'dictionary'})
props_dict.update({'description': 'Description of the input features.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'target_data_description'})
props_dict.update({'label': 'Target data description'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'dictionary'})
props_dict.update({'description': 'Description of the target values.'})
props.append(props_dict)
#---------------------------------------------------
new_model_dict.update({'properties': props})
cat.append(new_model_dict)
#########################################################################

#########################################################################
new_model_dict = {}
new_model_dict.update({'id': 30})
new_model_dict.update({'POM': 6})
new_model_dict.update({'type': 'clustering'})
new_model_dict.update({'name': 'Kmeans'})
new_model_dict.update({'label': 'Kmeans clustering'})
new_model_dict.update({'description': 'Kmeans clustering algorithm.'})
props = []
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'Nmaxiter'})
props_dict.update({'label': 'Max number of iterations.'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Max number of epochs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'NC'})
props_dict.update({'label': 'Number of centroids'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Number of centroids'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'conv_stop'})
props_dict.update({'label': 'Convergence threshold to stop training.'})
props_dict.update({'defaultValue': 0.005})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Convergence threshold to stop training.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'input_data_description'})
props_dict.update({'label': 'Input data description'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'dictionary'})
props_dict.update({'description': 'Description of the input features.'})
props.append(props_dict)
#---------------------------------------------------
new_model_dict.update({'properties': props})
cat.append(new_model_dict)
#########################################################################


#########################################################################
new_model_dict = {}
new_model_dict.update({'id': 31})
new_model_dict.update({'POM': 6})
new_model_dict.update({'type': 'regression'})
new_model_dict.update({'name': 'KR'})
new_model_dict.update({'label': 'Kernel Regression'})
new_model_dict.update({'description': 'Kernel Regression model using Gaussian kernels.'})
props = []
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'Nmaxiter'})
props_dict.update({'label': 'Max number of iterations.'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Max number of epochs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'input_data_description'})
props_dict.update({'label': 'Input data description'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'dictionary'})
props_dict.update({'description': 'Description of the input features.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'fsigma'})
props_dict.update({'label': 'Sigma factor.'})
props_dict.update({'defaultValue': 0.1})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Factor to obtain the sigma value as fsigma * sqrt(NI), where NI is the number of inputs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'C'})
props_dict.update({'label': 'Centroids.'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'matrix'})
props_dict.update({'description': 'Centroids to be used for the computation of the kernels, row-wise stored to build a NCxNI matrix.'})
props.append(props_dict)
#---------------------------------------------------
new_model_dict.update({'properties': props})
cat.append(new_model_dict)
#########################################################################


#########################################################################
new_model_dict = {}
new_model_dict.update({'id': 32})
new_model_dict.update({'POM': 6})
new_model_dict.update({'type': 'classification'})
new_model_dict.update({'name': 'BSVM'})
new_model_dict.update({'label': 'Budget Support Vector Machine'})
new_model_dict.update({'description': 'Support Vector Machine model with controlled complexity (budget) using Gaussian kernels.'})
props = []
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'Nmaxiter'})
props_dict.update({'label': 'Max number of iterations.'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Max number of epochs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'conv_stop'})
props_dict.update({'label': 'Convergence threshold'})
props_dict.update({'defaultValue': 0.005})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Convergence value to stop training.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'Csvm'})
props_dict.update({'label': 'Error penalty'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Penalization of every nonzero slack variable.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'input_data_description'})
props_dict.update({'label': 'Input data description'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'dictionary'})
props_dict.update({'description': 'Description of the input features.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'fsigma'})
props_dict.update({'label': 'Sigma factor.'})
props_dict.update({'defaultValue': 0.1})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Factor to obtain the sigma value as fsigma * sqrt(NI), where NI is the number of inputs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'C'})
props_dict.update({'label': 'Centroids.'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'matrix'})
props_dict.update({'description': 'Centroids to be used for the computation of the kernels, row-wise stored to build a NCxNI matrix.'})
props.append(props_dict)
#---------------------------------------------------
new_model_dict.update({'properties': props})
cat.append(new_model_dict)
#########################################################################

#########################################################################
new_model_dict = {}
new_model_dict.update({'id': 33})
new_model_dict.update({'POM': 6})
new_model_dict.update({'type': 'classification'})
new_model_dict.update({'name': 'MBSVM'})
new_model_dict.update({'label': 'Multiclass Budget Support Vector Machine'})
new_model_dict.update({'description': 'Support Vector Machine model with controlled complexity (budget) using Gaussian kernels.'})
props = []
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'Nmaxiter'})
props_dict.update({'label': 'Max number of iterations.'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Max number of epochs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'conv_stop'})
props_dict.update({'label': 'Convergence threshold'})
props_dict.update({'defaultValue': 0.005})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Convergence value to stop training.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'Csvm'})
props_dict.update({'label': 'Error penalty'})
props_dict.update({'defaultValue': 10})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Penalization of every nonzero slack variable.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'input_data_description'})
props_dict.update({'label': 'Input data description'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'dictionary'})
props_dict.update({'description': 'Description of the input features.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'target_data_description'})
props_dict.update({'label': 'Target data description'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'dictionary'})
props_dict.update({'description': 'Description of the target values.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'fsigma'})
props_dict.update({'label': 'Sigma factor.'})
props_dict.update({'defaultValue': 0.1})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Factor to obtain the sigma value as fsigma * sqrt(NI), where NI is the number of inputs.'})
props.append(props_dict)
#---------------------------------------------------
props_dict = {}
props_dict.update({'name': 'C'})
props_dict.update({'label': 'Centroids.'})
props_dict.update({'defaultValue': None})
props_dict.update({'type': 'matrix'})
props_dict.update({'description': 'Centroids to be used for the computation of the kernels, row-wise stored to build a NCxNI matrix.'})
props.append(props_dict)
#---------------------------------------------------
new_model_dict.update({'properties': props})
cat.append(new_model_dict)
#########################################################################

with open('MMLL_catalogue.json','w') as f:
    json.dump(cat, f)


print('=================================')
for model in cat:
    print('id = ', model['id'])
    print('POM = ', model['POM'])
    print('type = ', model['type'])
    print('name = ', model['name'])
    print('label = ', model['label'])
    print('description = ', model['description'])
    print('properties:')
    props_dict = model['properties']
    for prop in props_dict:
        print('\t' + prop['name'] + ', ' + prop['type'] + ', ' + str(prop['defaultValue']) + ', ' + prop['label'] + ', ' + prop['description'])   
    print('=================================')


import code
code.interact(local=locals())

