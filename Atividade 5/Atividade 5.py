#Importação dos pacotes e bibliotecas 
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from sklearn import datasets
from sklearn.model_selection import train_test_split 
import keras
from keras import layers as kl
from keras import Sequential
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import numpy as np
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

#Carreando o dataset iris

iris = datasets.load_iris()

#Verificando os atributos que compoem o dataset

#print(iris.feature_names,"\n")
#print("\n",iris.target_names,"\n")

#Verificando como os dados estão dispostos

#print(iris.data)

#Armazenando os dados para a previsão em X

X = iris.data

#Armazenando as respostas (ou target) em Y 

Y = iris.target

#Verificando o tamanho dos dados

#print("Shape of X data: ", X.shape)
#print("Shape of Y data: ", Y.shape)

X_train, X_test, Y_test, Y_train = train_test_split(X, Y, test_size= .2)

#Construção do modelo

model = Sequential()
model.add(kl.Dense(100, activation = 'relu', input_shape=(4, )))
model.add(kl.Dense(30, activation = 'relu'))
model.add(kl.Dense(60, activation = 'relu'))
model.add(kl.Dense(3, activation = 'relu'))

model.summary()