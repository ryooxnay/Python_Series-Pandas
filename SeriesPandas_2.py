# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 06:59:53 2022

https://www.youtube.com/watch?v=IBMrXyTR6CU&list=PLat2DtY8K7YUFy8OwcwzcoicZjk4sqVZX&index=6
Correlacion

"""
#'' % \ &|~

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder

personas = pd.read_csv("personas.csv")

#Relacion  PESO Y TALLA
def rela_1G():
    plt.scatter(personas["altura"], personas["peso"])
    plt.xlabel("Altura (cms)")
    plt.ylabel("Peso (Kgs)")
    plt.show()

#RELACION DE INFRESO Y HORAS TRABAJADAS
def rela_2G():
    plt.scatter(personas["ingreso"], personas["horas_trabajadas"],color='red')
    plt.xlabel("Ingresos ($)")
    plt.ylabel("Horas Trabajadas")
    plt.show()
def rela_3G():
    plt.scatter(personas["ingreso"], personas["ausencias"],color='black')
    plt.xlabel("Ingresos ($)")
    plt.ylabel("Ausencias")
    plt.show()
def rela_4G():
    plt.scatter(personas["ingreso"], personas["peso"],color='red')
    plt.xlabel("Ingresos ($)")
    plt.ylabel("Peso (Kgs)")
    plt.show()
def relacio():
    # -1 Relacion fuerte negativa  (Los datos decaen) 
    # 1 Relacion fuerte positiva   (Los datos van en aumento)
    print(personas.corr())
def matriz_rela():
    matriz = personas.corr()
    plt.matshow(matriz, cmap="bwr", vmin=-1, vmax=1) # cmap = -1 azul, 0 blanco, 1 rojo
    #Nombres a las fraficas
    plt.xticks(range(5),personas.columns, rotation=90)
    plt.yticks(range(5),personas.columns)
    for i in range(len(matriz.columns)):
        for j in range(len(matriz.columns)):
            plt.text(i,j, round(matriz.iloc[i,j],2), ha="center", va="center")
            # metodo .iloc es para ceder a valores dentro de una matriz
    plt.colorbar()
    plt.show()

# Poner una columna en fila para mejorar la visualizacion de los datos
def codificasion():
    datos = {"nombre":["Maria","Ana", "Elsa", "Gustavo","Pedro", "Raul", "Carlos", "Jose", "Luis"],
             "saldo":[10000.00, 800.00, 9000.00, 2000.00, 2100.00, 12000.00, 5000.00, 10000.00, 200.00],
             "pais":["Argentina","Bolivia","Chile","Colomia","Costa Rica","Ecuador","Mexico","Peru","Peru"]}
    
    datos = pd.DataFrame(datos)
    datos["pais"] = datos["pais"].astype("category")
    codificador = OneHotEncoder()
    codificacion = codificador.fit_transform(datos[["pais"]])
    nuevas_cols = pd.DataFrame(codificacion.toarray(),columns=codificador.categories_)
    datos = pd.concat([datos, nuevas_cols], axis="columns")
    print(datos)


### 
def ordinales():
    categorias_s = ["Muy insatisfecho", "Insatisfecho", "Neutral", "Satisfecho", "Muy satisfecho"]
    categorias_c = ["Muy mala","Mala", "Buena", "Muy buena", "Exelente"]
    encuesta = {"servicio":["Muy insatisfecho", "Insatisfecho", "Neutral", "Satisfecho", "Muy satisfecho", "Muy insatisfecho"],
                "alimentos":["Mala", "Buena", "Muy mala", "Exelente", "Mala", "Buena"]}
    tipo_c = [0,0,1,1,0,1]  #0: cliente esporadico   1: cliente frecuente
    #print(pd.DataFrame(encuesta))
    def codifi_ordinal():
        datos_ord = pd.DataFrame(encuesta)
        codifica = OrdinalEncoder(categories = [categorias_s, categorias_c])
        datos_ord = pd.DataFrame(codifica.fit_transform(datos_ord),columns=["servicio", "alimentos"])
        print(datos_ord)
    codifi_ordinal()
    
def categorias_1():
    edades = np.array([1,7,8,15,16,28,35,50,55,75,80,100])
    resultado = pd.cut(edades, 
                       bins=3,
                       labels=["baja","media", "alta"],
                       retbins=True)
    print(resultado[1],"\n")
    print(resultado[0].codes,"\n")
    print(resultado[0].categories,"\n")
    print(np.array(resultado[0]),"\n")
def categorias_2():
    edades = np.array([1,7,8,15,16,28,35,50,55,75,80,100])
    resultado = pd.cut(edades, 
                       bins=[0,11,17,59, np.inf],
                       labels=["infante","joven", "adulto","mayor"],
                       retbins=True)
    print(resultado[1],"\n")
    print(resultado[0].codes,"\n")
    print(resultado[0].categories,"\n")
    print(np.array(resultado[0]),"\n")
categorias_2()

    
    
    
    
    
    
    
    
    
    
    
    
    
    