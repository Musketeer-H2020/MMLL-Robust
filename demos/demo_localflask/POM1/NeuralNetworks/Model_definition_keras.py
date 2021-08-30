# -*- coding: utf-8 -*-
'''
Neural Network model definition using Tensorflow Keras
'''

__author__ = "Marcos Fernández Díaz"
__date__ = "February 2021"

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten

# Define Keras model architecture
model = Sequential()
model.add(Dense(5, input_shape=(11,), activation='relu'))
model.add(Dense(1, activation='linear'))

# Save the model architecture in JSON format
filename = 'keras_model_redwine_raw.json'
model_json = model.to_json()
with open(filename, "w") as json_file:
    json_file.write(model_json)

print('Model architecture %s saved to disk' %filename)
model.summary()
