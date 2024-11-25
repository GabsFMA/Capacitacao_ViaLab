#Importação das bibliotecas

from sklearn import datasets
import collections
import numpy as np

#Carregando o dataset Iris

iris = datasets.load_iris()

#Armazenando os dados de X e Y 

X = iris.data
Y = iris.target
print(Y)

lastpos = np.where(Y == 2)[0][0] - 1

Y = Y[0: lastpos]
X = X[0: lastpos]
print(Y)

