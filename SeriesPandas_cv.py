# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 18:49:20 2022
@author: USER
https://www.youtube.com/watch?v=uGx0PHD6o9M&t=682s
"""
import pandas as pd
ventas = pd.read_csv("ventas.csv", index_col=0, sep=";") #Sep para usar el tipo de separado, ya sea ; o $ entre otros caracteres
def inicio():
    ven = pd.read_csv("ventas.csv", index_col=0, usecols=[0,2,4], sep=";")
    print(ven)
def inicio2():
    #Para archivos que no cuenta con titulos en las columnas
    ven = pd.read_csv("ventas_sinEca.csv", index_col=0, sep=";", header=None, names=["T1","T2","T3","T4"])
    print(ven)
def basura():
    # skiprows=1, skipfooter=1, engine="python" para eliminar una fila basura arriba y el el final del archivo
    #se esplica que estamos usando python o puede marcar advertencias
    ven = pd.read_csv("ventas_sinEca2.csv", index_col=0, sep=";", header=None, names=["T1","T2","T3","T4"], skiprows=1, skipfooter=1, engine="python")
    print(ven)
def exel():
    exel = pd.read_excel("ventas_anuales.xlsx", index_col=0, skiprows=1, sheet_name="2021")
    print(exel)
exel()
"""
https://www.youtube.com/watch?v=Ys02DmUwl30&list=PLat2DtY8K7YUFy8OwcwzcoicZjk4sqVZX&index=4
"""