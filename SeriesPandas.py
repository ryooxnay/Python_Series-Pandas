# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 20:26:53 2022
https://www.youtube.com/watch?v=E7Tt458sTUE&list=PLat2DtY8K7YUFy8OwcwzcoicZjk4sqVZX&index=1&t=558s
@author: Series de Pandas: Análisis de Datos con Python
"""

import pandas as pd

#'' % \
nombre=["Yony", "Roxa", "Kaily", "Yen", "Jenny", "Juan", "Silvia"]
edad=[29,22,2,22,19,54,51]
def unirLista():
    edades = pd.Series(edad, nombre) #(1,2) 1= Principal cadenan, 2= 
    print(edades)
    print("************")
    print(edades.dtypes)  #Para saber el tipo de dato
    print(edades.size)      #Para saber cuantos datos son
    print(edades.index)     #Para saber el encabesado de cada columna
    print(edades.values)    #Los valores de los encabesados
    print("************")
def interacion():
    edades = pd.Series(edad, nombre)
    for elemento in edades:
        print(elemento)
    for elemento in edades.index:
        print(elemento)
    print(edades["Yony"],"\n", edades[["Yony", "Kaily"]])
    print("############")
    print(edades[0],"\n", edades[0:2],"\n", edades[[0,2]])
def cambioTipoDato():
    edades = pd.Series(edad, nombre)
    print(edades.astype("float"))
    print(edades.astype("i2"))      #Cambia los datos a valores de dos bits, para la esdades es perfecto
    print(edades.value_counts())    #Cuenta cuantos vaores tienen el mismo dato
    edades.sort_values(inplace=True) #para ordenar los valores de mayor a menor.  
    #implace=True es para guardar la lista ordenada, puede no tenerla y no se guardan los cambios
    print(edades)
    edades.sort_index(inplace=True)
    print(edades)
def opera_vectoriales():
    edades = pd.Series(edad, nombre)
    print(edades + 1)
    print("EL mas viejo es de ", edades.max())
    print("Se encuentra en la posicion ", edades.argmax())
    print("El mas joven es de ", edades.min())
    print("Se encuentra en la pocsicion", edades.argmin())
    print("el promedio de la edades des de ", edades.sum()/edades.size, "  Solo la suma es de ", edades.sum())
def opera_estadis():
    edades = pd.Series(edad, nombre)
    print("Moda = ", edades.mode())     #El valor que mas se repite
    print("Promedio = ", edades.mean()) #Promedio
    print("Mediana = ", edades.median()) #El valor mediano
    print("Medida estandar = ", edades.std())   #Desviacion estandar, es un amedida de dispercion
    print("Cuantos datos son = ", edades.count())  #Metodo Count() es para contar cuantos son
def describir():
    edades = pd.Series(edad, nombre)
    print(edades.describe())
    print("Quantiles 25% = ", edades.quantile(0.25))
    print("Quantiles 50% = ", edades.quantile(0.5))
    print("Quantiles 75% = ", edades.quantile(0.75))
    print("Quantiles 100% = ", edades.quantile(1))
def graficas():
    edades = pd.Series(edad, nombre)
    edades.plot()
graficas()
#interacion()