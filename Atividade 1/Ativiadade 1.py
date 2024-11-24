##Importação das bibliotecas

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 

##Importação do dataset

wine_quality_red = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep=';')
wine_quality_red.head(10)

wine_quality_white = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv', sep=';')
wine_quality_white.head(10)

wine_quality_concat = pd.concat ([wine_quality_red, wine_quality_white])

final_red = pd.DataFrame()
final_red = wine_quality_red.iloc[1592: ]

##final_white = pd.DataFrame()
final_white = wine_quality_white.iloc[4891: ]

##Descobrir quantos valores nulos existem em cada coluna

##for column in wine_quality_concat:
##    nulos = wine_quality_concat[column].isnull().sum()
##   print("A coluna: ", column, " possui ", nulos, " valores nulos")
    
##Descobrir dados detalhados do DataSet

def detalhes (dataf):
    for col in dataf:
        nulos = dataf[col].isnull().sum()
        print ("A coluna: ", col, " possui ", nulos, "valores nulos")
        not_a_number = dataf[col].isna().sum()
        print ("A coluna: ", col, " possui ", not_a_number, "valores NaN")
        valores = dataf[col].describe().iloc[0]
        print ("A coluna: ", col, "possui ", valores, " valores numéricos")
        media = dataf[col].describe().iloc[1]
        print ("A coluna: ", col, " tem como media o valor: ", media,2)
        desvio = dataf[col].describe().iloc[2]
        print("Seu desvio padrão é: ", desvio)
        print("=======================")

##detalhes (wine_quality_concat)

lista = []
lista = wine_quality_concat['quality']
lista.value_counts()


wine_quality_concat.shape[1]