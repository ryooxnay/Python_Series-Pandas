# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 15:55:33 2022

@author: USER
"""


import pandas as pd
import numpy as np
datos = pd.read_csv("dataset.csv", index_col="id") #la Colimna ID sea la primera columna
print(datos)


print(datos.head())     #paara mostrar las primeras 5 filas 
print(datos.tail(10))   #para mostrar las ultimas 10 filas

print(datos.describe())
# mean -> Media
# std -> Desviacion estandar
# min -> Valor minimo
# Max -> Valor Maximo

filtro_Sin_Na = datos.dropna()   # Elimar los datos faltantes
print(filtro_Sin_Na)

datos_Na = datos.isna().sum() #isna() para mostrar los datos vacion 
print(datos_Na)   # .sum() Para mostar cuantos datos nulos se encuentan en cada columna
