import os
import numpy as np
import json
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_datasets as tfds

class NeuralNetwork:
    def __init__(self):
        super().__init__()
        
        with open("./data/Network/test.txt","r", encoding='utf8') as f:
            test_data = [tuple(i.split(',')) for i in f]
        with open("./data/Network/validation.txt","r", encoding='utf8') as f:
            validation_data = [tuple( i.split(',')) for i in f]
        with open("./data/Network/train.txt","r", encoding='utf8') as f:
            train_data = [tuple(i.split(',')) for i in f]

        test_data=np.array(test_data)
        validation_data=np.array(validation_data)
        train_data=np.array(train_data)

        print(type(test_data))
        print(test_data)



        embedding = "https://tfhub.dev/google/nnlm-en-dim50/2"
        hub_layer = hub.KerasLayer(embedding, input_shape=[], 
                                   dtype=tf.string, trainable=True)

        model = tf.keras.Sequential()
        model.add(hub_layer)
        model.add(tf.keras.layers.Dense(16, activation='relu'))
        model.add(tf.keras.layers.Dense(1))

        model.summary()

        model.compile(optimizer='adam',
            loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
            metrics=['accuracy'])

        history = model.fit(train_data,
            epochs=10,
            validation_data=validation_data,
            verbose=1)

    def Test(self,data):
        return 0
    def Learn(self):
        return 0
    def Analyse(self,data):
        return 1