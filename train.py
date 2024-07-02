# -*- coding: utf-8 -*-
"""train.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18JElvb1l1Cq4jo7x75Iw8avU2y40_r-0
"""
import os
import sys

if sys.stdout is None:
    sys.stdout = open(os.devnull, "w")
if sys.stderr is None:
    sys.stderr = open(os.devnull, "w")

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,Dropout
from chatbot_main import train_Y, train_X, bag_of_words
import numpy as np

model = Sequential()
model.add(Dense(256, input_shape=(len(train_X[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_Y[0]), activation="softmax"))

adam = tf.keras.optimizers.Adam(learning_rate=0.001)
def model_compile(loss, optimizer, metrics):
  model.compile(loss=loss, optimizer=optimizer, metrics=metrics)

model_compile(loss='categorical_crossentropy',
              optimizer=adam,
              metrics=['accuracy'])
print(model.summary())
model.fit(x = train_X, y = train_Y, epochs=150, verbose = 1)

def pred_class(text,vocab,labels):
  bow=bag_of_words(text,vocab)
  result=model.predict(np.array([bow]))[0]
  thresh=0.5
  y_pred=[[indx,res] for indx,res in enumerate(result) if res>thresh]
  y_pred.sort(key=lambda x:x[1],reverse=True)
  return_list=[]
  for r in y_pred:
    return_list.append(labels[r[0]])
  return return_list