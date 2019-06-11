#!/usr/bin/python3
#Bibliotecas importadas para usar 
from sklearn import cluster

#Corpus a clasificar, de goles y asistencias de un jugado
golesAsistencias=[[20,12],[30,16],[0,1],[1,0],[1,16],[2,16],[1,12],[2,14],[20,3],[18,1],[17,0],[20,3],[33,20]]

#Usamos algoritmo KMeans de Clustering, suponiendo 4 clusteres
# https://en.wikipedia.org/wiki/K-means_clustering
k_means = cluster.KMeans(n_clusters=4)

#Entrenamos el modelo
k_means.fit(golesAsistencias) 

#obtemos en values "los centros" de cada grupo
values = k_means.cluster_centers_.squeeze()
print("Valores Centros")
print(values)


#Obtenemos las etiquetas de cada prediccion del entrenamiento
labels = k_means.labels_
print("Etiquetas")
print(labels)

#Ejemplo de predecir un nuevo valor, a ver en que cluster iria
res=k_means.predict([[34,1]])
print("Prediccion")
print(res)