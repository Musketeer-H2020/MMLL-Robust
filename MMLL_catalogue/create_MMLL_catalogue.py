# -*- coding: utf-8 -*-

'''
python3 create_MMLL_catalogue.py


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

POM 1:
1 Kmeans
2 NeuralNetworks
3 SVM
4 DSVM

POM 2:
5 Kmeans
6 NeuralNetworks
7 SVM

POM 3:
8 Kmeans
9 NeuralNetworks
10 SVM

POM 4:
11 Kmeans
12 LR

POM 5:
13 Kmeans
14 LR

POM 6:
15 RR
16 Kmeans_pm
17 KR_pm
18 LC_pm
19 MLC_pm

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
####################   POM 5   ##########################################
#########################################################################



#########################################################################
####################   POM 6   ##########################################
#########################################################################


#########################################################################
new_model_dict = {}
new_model_dict.update({'id': 16})
new_model_dict.update({'POM': 6})
new_model_dict.update({'type': 'clustering'})
new_model_dict.update({'name': 'Kmeans_pm'})
new_model_dict.update({'label': 'Kmeans clustering'})
new_model_dict.update({'description': 'Kmeans clustering, public model.'})
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
new_model_dict.update({'properties': props})
cat.append(new_model_dict)
#########################################################################
#########################################################################
new_model_dict = {}
new_model_dict.update({'id': 18})
new_model_dict.update({'POM': 6})
new_model_dict.update({'type': 'classification'})
new_model_dict.update({'name': 'LC_pm'})
new_model_dict.update({'label': 'Logistic Classifier'})
new_model_dict.update({'description': 'Logistic Classifier, public model'})
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
props_dict.update({'name': 'regularization'})
props_dict.update({'label': 'Regularization parameter.'})
props_dict.update({'defaultValue': 0.001})
props_dict.update({'type': 'number'})
props_dict.update({'description': 'Regularization parameter.'})
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

