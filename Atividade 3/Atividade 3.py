#Importação das bibliotecas importantes para ML

import tensorflow as tf #Biblioteca com ferramentas para aprendizado de máquina
from sklearn.model_selection import train_test_split, cross_val_score
import matplotlib.pyplot as plt 
import keras  #Biblioteca usada para criação de redes neurais  
from keras.datasets import imdb #Conjunto de dados presente no Keras
import pandas as pd

#Ferramentas específicas do Keras

from keras.models import Sequential #Importação de tipo de modelo - Sequencial
from keras.layers import Dense, Dropout, Input, Flatten, Conv2D, MaxPooling2D#Importando tipos de camadas para rede neural nem todas serão utilizadas
from tensorflow.keras.utils import to_categorical

#Importação do DataSet a ser usada 

Wine_quality_red = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep=';')
Wine_quality_red.head(10)

##Divisão de dados

#Dados de treino: Conjunto de dados usado para treinar e fazer o modelo aprender os padões dos dados
#Dados de teste: Conjunto de teste é um conjunto separado de dados usado para testar o modelo após a 
# conclusão do treinamento e verificar se aquele modelo consegue generalizar os problemas ou se apenas
# decorou durante o processo de treino

#Os dados são tratados de para ML como X e Y, onde X é o conjunto de dados sem a variável
# de interesse e Y é apenas a variável de interesse

##Atividade) Dividir o dataset em 30% teste e 70% treino / Separar o X e Y de treino e o X e Y de teste / Normalização de dataset

print(Wine_quality_red.head())

X = Wine_quality_red.drop(columns=['quality'])
Y = Wine_quality_red['quality']

X_treino, X_teste, Y_treino, Y_teste = train_test_split(X, Y, test_size=0.3, random_state=42)

print("Tamanho do conjunto de treino: ", X_treino.shape)
print("Tamanho do conjunto de teste: ", X_teste.shape)