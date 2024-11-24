import numpy as np

##Conversão para numpy arrays 
arr = np.array([1,2,3])
##print(arr)

##Converter números para float
np.float32(345.8)

##Exibindo tipos de dado
arr.dtype

##Convertendo valores de uma array para float
np.array([1,2,3], dtype= 'f')

##Exercicios

##1) Criar um array com uma dimensão (1D) com o numpy

array_1D = np.array([1, 2, 3, 4, 5])

##print(array_1D)

##2) Crie uma array 5x5 usando Numpy

##Criando na mão
array_5x5 = np.array([[0, 1, 2, 3, 4],
                      [5, 6, 7, 8, 9],
                      [5, 6, 7, 8, 9],
                      [5, 6, 7, 8, 9],
                      [5, 6, 7, 8, 9]])

#print (array_5x5)

##Criando com números aleatórios

array_5x5_rand = np.random.rand(5,5)
#(array_5x5_rand)

##3) Converter o array 1D para 2D

##Convertendo para 1 linha e 5 colunas
array_2D_row = array_1D.reshape(1, 5)
#print("\nArray 2D (1 linha e 5 colunas): ")
#print(array_2D_row)

##Convertendo para 5 linhas 3 1 colunas
array_2D_col = array_1D.reshape(5, 1)
#print("\nArray 2D (5 linhas e 1 colunas): ")
#print(array_2D_col)

##4) Gere 2 array aleatório 3x4 e veja se há elementos em comum entre eles usando o Numpy

array_3X4_1 = np.random.randint(0, 21, (3,4))
array_3X4_2 = np.random.randint(0, 21, (3,4))
#print(array_3X4_1)
#print(array_3X4_2)

elementos_comuns = np.intersect1d(array_3X4_1, array_3X4_2)
#print("Elementos em comum", elementos_comuns)

def find_same_elements (array1, array2):
    if elementos_comuns.size > 0:
        print("Valores comuns encontrados")
        print("Elementos comuns: ", elementos_comuns)
    else:
        print("Não foram encontrados valores em comuns entre as arrays")


#find_same_elements(array_3X4_1, array_3X4_2)   

##5)Criar uma matriz 3x3 e inserir uma condição
    
matriz_3X3 = np.random.randint(0, 11, (3,3))

print(matriz_3X3)

matriz_3X3[matriz_3X3 > 5] = 99

print(matriz_3X3)