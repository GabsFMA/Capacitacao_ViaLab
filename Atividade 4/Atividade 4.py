#Importação das bibliotecas

from sklearn.decomposition import PCA
from sklearn import datasets
import collections
import numpy as np
import matplotlib.pyplot as plt

#Carregando o dataset Iris

iris = datasets.load_iris()

#Armazenando os dados de X e Y 

X = iris.data
Y = iris.target
#print(Y)

lastpos = np.where(Y == 2)[0][0] - 1

Y = Y[0: lastpos]
X = X[0: lastpos]
#print(Y)

#Redução da dimensionalidade utilizando PCA 

n_components = 2

pca = PCA(n_components=n_components)

X = pca.fit_transform(X)

#print (X, Y)

plt.plot(X[:, 0], X[:, 1], 'o', color = "black")
#plt.show()

class Perceptron():
    def __init__(self, w, threshold, variation):
        self.w = w
        self.threshold = threshold
        self.variation = variation

    def Treinar(self, data):
        if not isinstance(data, (list, tuple)) or len(data) != 3:
            raise ValueError("Os dados devem ser uma lista ou tupla com 3 elementos: [x, y, resultado_esperado]")
        x, y, resultado_esperado = data
        print("Data - " + str(data))
        erro = self.Calcular([x, y], resultado_esperado)
        return erro


    def Calcular(self, entrada, resultado_esperado):
        # Calcula a saída do perceptron
        soma = self.w[0] + self.w[1] * entrada[0] + self.w[2] * entrada[1]
        
        # Função de ativação
        if soma >= self.threshold:
            saida = 1
        else:
            saida = 0

        # Calcula o erro
        erro = resultado_esperado - saida

        # Corrige os pesos se houver erro
        if erro != 0:
            self.Corrigir(entrada, erro)

        return erro

    def Corrigir(self, entrada, erro):
        # Atualiza os pesos (incluindo o bias)
        self.w[0] += self.variation * erro  # Atualiza o bias
        self.w[1] += self.variation * erro * entrada[0]  # Atualiza peso para x
        self.w[2] += self.variation * erro * entrada[1]  # Atualiza peso para y
        print("Pesos corrigidos: " + str(self.w))
        
p = Perceptron(w = [0,0,0], threshold=0.5, variation=0.1)

dados = [[1,0,1],[0,1,0], [1,1,1], [0,0,0]]

for d in dados:
    erro = p.Treinar(d)
    print(f"Erro: {erro}")