#!/usr/bin/python3
#Biblioteca para usar JSON
import json
#Biblioteca para usar "Maquinas de vector de soportel"
from sklearn import svm

# Biblioteca para importar/exportar el modelo entrenado
import joblib

#Biblioteca para usar funciones del sistema
import sys

#MAIN
#Si hay un segundo argumento, lo tomamos como el numero del JSON a leer (y modelo a entrenar)
if len(sys.argv)==2:
    numPart=int(sys.argv[1])
    #Si no ponemos valor por defecto, tomamos valor 1000
else:
    numPart=1000
    
print("Entrenando SVM con modelo de "+str(numPart)+" partidas")

#Cargamos el JSON de las partidas generadas
with open('../data'+str(numPart)+'.json') as file:
    data = json.load(file)

#En base a las partidas, creamos una lista de las features que queremos para cada ejemplo
# Ahi metemos los elementos de la partida del 0 al 10
features=[]
for i in range(len(data)):
    features.append(data[i][:11])


#En base a cada partida, creamos una etiqueta con el valor almacenado en la posicion 11
#0 Derrota, 1 Victoria
labels=[]
for i in range(len(data)):
    labels.append(data[i][11])

# Creamos clasificador de maquina de vectores de soporte https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
# Maquinas de vectores de soporte  https://es.wikipedia.org/wiki/M%C3%A1quinas_de_vectores_de_soporte
classif = svm.SVC(gamma=0.001, C=100.)
classif.fit(features, labels)
#Salvamos el modelo entrenado
joblib.dump(classif, 'modelTree3EnRaya'+str(numPart)+'.pkl') 

#Para probar rapido la clasificacion
#print (classif.predict([[0, 0, 0, 0, 0, 0, 0, 1, 0, 4, 1]]))

