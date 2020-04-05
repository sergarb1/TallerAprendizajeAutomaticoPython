#incluiamos de sklearn modelos lineal
from sklearn import linear_model
#Biblioteca para usar JSON
import json
# Biblioteca para importar/exportar el modelo entrenado
import joblib


#Cargamos el modelo de regresion lineal
lr = joblib.load('modeloRegresion.pkl') 

while(True):
    print("Introduzca los metros de su piso:")
    metros=int(input())
    precioPred = lr.predict([[metros]])
    print("Su piso esta valorado en "+str(int(precioPred[0][0]))+ " Euros")
