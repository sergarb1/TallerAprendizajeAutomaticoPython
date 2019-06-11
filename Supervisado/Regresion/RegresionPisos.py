#!/usr/bin/python3

#incluiamos de sklearn modelos lineal
from sklearn import linear_model

#Ejemplos de entrenamiento
# Caracteristicas (metrosPiso)
metrosPisos=[[50],[100],[120],[150],[400],[95],[90]]
# Valores asociados (precioPiso)
precioPisos=[[30000],[120000],[140000],[150000],[300000],[100000],[110000]]


#Utilizamos LinearRegression, que es regresion lineal por mínimos cuadrados
#https://sites.google.com/site/numerictron/unidad-4/4-3-regresion-por-minimos-cuadrados-lineal-y-cuadratica
lr = linear_model.LinearRegression()

#Entrenamos el modelo de regresion linea
lr.fit(metrosPisos,precioPisos)

#Probamos con rangos desde 50 a 200 de 10 en 10 e intentamos predecir precio
for i in range(50,200,10):
    print("Piso de "+str(i)+" metros")
    print("Predecimos precio:")
    precioPred = lr.predict([[i]])
    print(int(precioPred)+ " Euros")
