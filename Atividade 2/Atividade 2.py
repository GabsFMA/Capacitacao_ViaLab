import numpy as np
import matplotlib.pyplot as plt

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

#print(matriz_3X3)

matriz_3X3[matriz_3X3 > 5] = 99

#print(matriz_3X3)

##6) Elabore um funação em python que realize pelos menos 3 funções matemáticas com funções numpy
 
def mat_op(array1, array2):  
    
    print("As arrays trabalhadas serão: \n", array1, "\n e \n", array2, "\n")
      
    soma_array = array1 + array2
    print("Soma das arrays: \n", soma_array, "\n")
    subtrai_array = array1 - array2
    print("Subtração das arrays\n", subtrai_array, "\n")
    multiplica_array = array1 * array2
    print("Produto das arrays\n", multiplica_array, "\n")


#mat_op(array_3X4_1, array_3X4_2)

##7) Crie duas matrizes, realize a multiplicação delas por meio de funções numpy e tente encontrar elemento em comum.

matriz1 = np.random.randint(0, 10, (2,2))
matriz2 = np.random.randint(0, 10, (2,2))

matriz_produto = matriz1 * matriz2

def valores_comuns(matriz1, matriz2, matriz_produto):
    
    if np.intersect1d(matriz1, matriz2).size > 0:
        print("Foram encontrados elementos comuns entre as matrizes 1 e 2!\n")
    else:
        print("Não foram encontrados valores em comum entre as matrizes 1 e 2!\n")
    
    if np.intersect1d(matriz1, matriz_produto).size > 0:
        print("Foram encontrados elementos comuns entre a matrizes 1 e a matriz produto!\n")
    else:
        print("Não foram encontrados valores em comum entre a matrizes 1 e a matriz produto!\n")    

    if np.intersect1d(matriz_produto, matriz2).size > 0:
        print("Foram encontrados elementos comuns entre a matriz produto e a matriz 2!\n")
    else:
        print("Não foram encontrados valores em comum entre a matriz produto e a matriz 2!\n")
        
#valores_comuns(matriz1, matriz2, matriz_produto)

##8) Elabore dois arrays 1D e os concatene

array_1D_1 = ([1, 2, 3])
array_1D_2 = ([4, 5, 6])

array_1D_contanedado = np.concatenate((array_1D_1, array_1D_2))

#print("Array concatenada: ", array_1D_contanedado)

##9) Gere duas matrizes 5x5, uma de zeros(0) e outra de uns(1), utilizando apenas funções numpy.

matriz_5x5_0 = np.zeros((5,5))
matriz_5x5_1 = np.ones((5,5))

#print(matriz_5x5_0, "\n")
#print("\n", matriz_5x5_1)

#10) Gere um array 1D, realize as operações de seno e cosseno por meio de pacotes numpy e plot os resultados.

sen = np.sin(array_1D_1)
cos = np.cos(array_1D_1)

print("Seno:", sen)
print("Cosseno: ", cos)

plt.plot(array_1D_1, sen, label = 'Seno', color = 'blue', linestyle = '-')
plt.plot(array_1D_1, cos, label = 'Cosseno', color = 'red', linestyle = '--')
plt.title('Valores de Seno e Cosseno', fontsize=16)
plt.xlabel('x (radianos)', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.grid(alpha=0.3)
plt.legend(fontsize=12)
plt.show()