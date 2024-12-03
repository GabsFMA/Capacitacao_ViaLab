# Importação dos pacotes e bibliotecas
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from sklearn import datasets
from sklearn.model_selection import train_test_split
import keras
from keras import layers as kl
from keras import Sequential
from keras.layers import Input
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import numpy as np
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

# Carregando o dataset iris
iris = datasets.load_iris()

# Verificando os atributos que compõem o dataset
# print(iris.feature_names, "\n")
# print("\n", iris.target_names, "\n")

# Verificando como os dados estão dispostos
# print(iris.data)

# Armazenando os dados para a previsão em X
X = iris.data

# Armazenando as respostas (ou target) em Y
Y = iris.target

# Verificando o tamanho dos dados
# print("Shape of X data: ", X.shape)
# print("Shape of Y data: ", Y.shape)

# Divisão dos dados em treino e teste
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Construção do modelo
model = Sequential()  # Inicialização do modelo
model.add(Input(shape=(4,)))  # Define a entrada do modelo
model.add(kl.Dense(100, activation='relu'))  # Primeira camada densa
model.add(kl.Dense(30, activation='relu'))  # Segunda camada densa
model.add(kl.Dense(60, activation='relu'))  # Terceira camada densa
model.add(kl.Dense(3, activation='softmax'))  # Camada de saída com softmax para classificação multiclasses

# print(model.summary())  # Resumo do modelo (opcional)

# Compilação do modelo
model.compile(loss='sparse_categorical_crossentropy', optimizer='adamax', metrics=['accuracy'])

# Treinamento do modelo
hist = model.fit(X_train, Y_train, epochs=30, batch_size=32, verbose=1, validation_split=0.2)

# Exibição do histórico de treinamento
#print(hist)

#Gráfico de loss, erros do modelo. Menor é melhor

plt.figure(figsize=(10,8))
plt.title('Gráfico de Loss')
plt.xlabel('Epocs')
plt.ylabel('Valor')
plt.plot(hist.history['loss'], label = 'loss')
plt.plot(hist.history['val_loss'], label = 'val_loss')
plt.legend()
plt.show()