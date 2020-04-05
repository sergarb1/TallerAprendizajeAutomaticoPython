#!/usr/bin/python3

#Incluimos biblioteca para trabaja con JSON
import json

#Cargamos el JSON de los datos de la prediccion
with open('./dataPrediccion.json') as file:
    data = json.load(file)


print("Resumen con interpretacion nuestra")
#Tabla donde damos una etiqueta a cada prediccion
#La primera etiqueta es para la prediccion 0, luego la 1, etc...
TraduccionPosicion=["Asistente","Goleador","Goleador y asistente", "Nada"]

for i in range(len(data)):
    cad="Goles "+str(data[i][0])+ " Asistencias "+str(data[i][1])
    cad=cad+" =====> Prediccion:"+TraduccionPosicion[int(data[i][2])]
    print(cad)
    print("") 