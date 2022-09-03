
"""
Created on Sun Jul 24 20:28:05 2022
@author: USER
DataFrames de Pandas: Análisis de Datos con Python
https://www.youtube.com/watch?v=DjQyHmy9AqQ&list=PLat2DtY8K7YUFy8OwcwzcoicZjk4sqVZX&index=2&t=1735s
"""
#'' % \ &|~

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


nombre_paises = ["China", "india", "Estados Unidos", "Indonesia", "Pakistan",
                 "Brasil", "Nigeria", "Bangladesh","Rusia", "Mexico"]
encabezado = ["poblacion", "porcentaje"]
#Poblacion en millones 
datos = [[1439,18.47],[1380,17.70],[331,4.25],[273,3.51],
         [220,2.83],[212,2.73],[206,2.64],[164,2.11],[145,1.87],[128,1.65]]
datosB = {"China":[1439,18.47],"India":[1380,17.70],"Estados Unidos":[331,4.25],"Indonesia":[273,3.51]
          ,"Pakistan":[220,2.83],"Brazil":[212,2.73],"Nigeria":[206,2.64],"Bangladesh":[164,2.11]
          ,"Rusia":[145,1.87],"Mexico":[128,165]}
tasa_fertilidad=[1.7, 2.2, 1.8, 2.3, 3.6, 1.7, 5.4, 2.1, 1.8, 2.1]
def dataframe1():
    paises = pd.DataFrame(datos, index = nombre_paises, columns = encabezado)
    print(paises)
    #print(paises.dtypes)           #Para ver los tipos de valores
    #print(paises.values, paises.size)
    #print(paises.index, paises.columns)
    print(paises.poblacion)
    print(paises[["porcentaje", "poblacion"]])
    print(paises["poblacion"][0:5])
    # muestra el numero de la fila con pequeña decipcion,, puede ser un solo nunmero o (de, asta)
    print(paises.iloc[0:2], "\n") # nos regresa los valores de una grafica
    print(paises.loc["Mexico"])     # muestra dependiendo la fila que tenga el  " index "
    
def data_biblioteca():
    paises = pd.DataFrame(datosB, index=encabezado)
    print(paises.transpose())       #para cambiar las colimnas por las filas.
    print(paises.T)                 #Para cambiar las columnas por las filas.
def dataframe2():
    paises = pd.DataFrame(datos, index = nombre_paises, columns = encabezado)
    paises["poblacion"] = paises["poblacion"].astype("int") #Para cambiar el tipo de valor de una columna y si se iguala se guarda los cambiombios, si no solo sera el cambio temporal
    print(paises.info())            #pequeño resumen de lo que contiene
    print(paises.head(), "\n",  paises.tail())      #Nos muestra los primeros 5 filas y las ultimas 5 filas
    print(paises.sort_values(by=["porcentaje"]))    #Para ordenar los datos 
    print(paises.sort_index())              #para ordenar la columna por el nombre de titilo
    paises["tasa_fertilidad"] = tasa_fertilidad         #para agragar una columna a nuestro diccionario
    print(paises.sort_values(by=["tasa_fertilidad"]))
    print(paises.pop("tasa_fertilidad"))        #para borrar una columna del diccionario
    print(paises)
def dataframe3():
    paises = pd.DataFrame(datos, index = nombre_paises, columns = encabezado)
    renglon = pd.Series(name="Japon", data=[126,1.62], index=["poblacion", "porcentaje"])
    paises = paises.append(renglon)           #para agregar una fila a nuestro diccionaro, primero se crea el registro en un variable "renglon" ↖↖↖↖
    print(paises)
    #Para eliminar una fila, el    axis en 0 borra filas y el axis en 1 borra columnas y con el inplace es para que se guarden los cambios en el diccionario
    print(paises.drop(["Japon"], axis = 0, inplace=True))
    
#dataframe3()
#data_biblioteca()
#  ----  -
#  ----  -
#  -     - filtros
def ejemplo2():
    
    dat = {"pais":["Estados Unidos", "China","Brasil","India", "Mexico"],
           "km2":[9833517,9600000,8515767,3287263,1964375]}
    paises = pd.DataFrame(dat, index = dat["pais"])
    print(paises)
def DatosP():
    paises = pd.read_csv("datos_paise.csv", index_col=0)
    #print(paises)
    
    #Paises con superficie menor a 50
    KM2Menos50 = paises["km2"]<50
    #print(paises[KM2Menos50])
    
    #Superficies que Km2 sea menor a 50 ( Y ) tengan una poblacion mayor de 500
    print(paises[(paises["km2"]<50)&(paises["poblacion_miles"]>500)])
    
    #Paises con una superficie menor a 5 KM2 ( O ) con poblacion menor a 5
    menor = paises[(paises["km2"]<5)|(paises["poblacion_miles"]<5)]
    print(menor)
    
    #Paises Europeos con superficies menor a 50 km2  ( Y ) con poblacion menor a 50
    euro = paises[(paises["continente"]=="Europa")&(paises["km2"]<50)&(paises["poblacion_miles"]<50)]
    print(euro)
    
    Noeuro = paises[(paises["continente"]!="Europa")&(paises["km2"]<50)&(paises["poblacion_miles"]<50)]
    print(Noeuro)
    #filtro3 = paises["km2"] and pobla < 5
    #print(filtro3)
#######################################################################################    
    
    ###############    DATOS FALTANTES
#######################################################################################
def datos_falta():
    d = pd.read_csv('clientes_falta.csv', sep=";")
    print(d)
    
    #para ver los valores nulos
    #print(d[d["nombre"].isnull()])
    
    #Para eliminar todos los nullos
    #print(d.dropna())
    
    #Para eliminar todos los nullos de ciertas columnas
    #d.dropna(subset=["nombre", "ingreso"], inplace=True)
    #print(d)
    
    #para cambiar los valores nulos a 0
    print(d.fillna(0))
    
    #para cambiar los valores nulos de una columna en especifico
    print(d["nombre"].fillna("Desconocido"))
    #para cambiar los valores por medio de un diccionario
    valor_defec = {"nombre":"Desconocido", "edad":"18", "ingreso":"10000"}
    print(d.fillna(value=valor_defec))
    def promedios():
        prom = d["ingreso"].mean()
        media = d["ingreso"].median()
        moda = d["ingreso"].mode()[0]
        print("El promdio es : ",prom, "  La media es; ", 
              media, "  La moda es : ", moda)
        #como  llenar los datos faltantes utilizando el promedio o la moda de los demas valored de la columna
        print(d["ingreso"].fillna(moda))
    promedios()
    

    
datos_falta()

















