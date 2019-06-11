#!/usr/bin/python3

# Incluimos la biblioteca para trabajar con aleatorios
import random
#Incluimos biblioteca para trabaja con JSON
import json

# Funcion que recibe un tablero y devuelve true si ha ganado, false en caso contrario
def haGanado(tab):
    if(tab[0]!=0 and tab[0] == tab[1] and tab[1] == tab[2]):
        return True
    if(tab[3]!=0 and tab[3] == tab[4] and tab[4] == tab[5]):
        return True
    if(tab[6]!=0 and tab[6] == tab[7] and tab[7] == tab[8]):
        return True

    if(tab[0]!=0 and tab[0] == tab[3] and tab[3] == tab[6]):
        return True
    if(tab[1]!=0 and tab[1] == tab[4] and tab[4] == tab[7]):
        return True
    if(tab[2]!=0 and tab[2] == tab[5] and tab[5] == tab[8]):
        return True

    if(tab[0]!=0 and tab[0] == tab[4] and tab[4] == tab[8]):
        return True
    if(tab[2]!=0 and tab[2] == tab[4] and tab[4] == tab[6]):
        return True

    return False


# funcion que juega una partida aleatoria y guarda todas las jugadas
# Al finalizar, etiqueta las jugadas con quien ha ganado o perdido la partida
# o a los dos como perdedores si hay empate
# Devuelve las jugadas realizadas etiquetadas
def partidaAleatoria():
    # Definimos tablero inicial
    tablero = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    # Definimos turno inicial aleatoriamente
    turno = random.randint(1,2)
    # Definimos jugadas realizadas
    jugadas = 0

    # historico de jugadas, vacio, con dos listas
    historico = [[], []]

    while jugadas < 9:

        # obtenemos posicion y si esta ocupada repetimos
        posicion = random.randint(0, 8)
        while tablero[posicion] != 0:
            posicion = random.randint(0, 8)
        # Anotamos una jugada mas
        jugadas = jugadas+1

        # Almacenamos el historico, estado del tablero y a donde mueve
        muestra=tablero[:] + [posicion] +[turno]
        
        historico[turno-1].append(muestra)
        # Cambiamos el tablero
        tablero[posicion] = turno


        # Si la partida ha acabado en victoria
        if(haGanado(tablero)):
            # Marcamos como ganadores
            for i in range(len(historico[turno-1])):
                historico[turno-1][i].append(1)
            # Cambiamos turno
            if turno == 1:
                turno = 2
            else:
                turno = 1
            # Marcamos como perdedores
            for i in range(len(historico[turno-1])):
                historico[turno-1][i].append(0)

            res = historico[0] + historico[1]
            return res

        # Cambiamos turno
        if turno == 1:
            turno = 2
        else:
            turno = 1

    # Si llegamos aqui, hubo un empate y damos a los dos jugadores como perdedores
    for i in range(len(historico[0])):
        historico[0][i].append(0)
    for i in range(len(historico[1])):
        historico[1][i].append(0)
    res = historico[0] + historico[1]

    return res


# Aqui el main

#Definimos cuantas partidas vamos a jugar
nPartidas=1
data=[]
#Jugamos las partidas
for i in range (nPartidas):
    #Imprimmos el progreso cada 1000 partidas
    if i>=1000 and i%1000==0:
        print(i)
    #Anyadimos el valor de la partida aleatoria
    data = data + partidaAleatoria()

#Guardamos las partidas generadas en el fichero JSON
with open('data'+str(nPartidas)+'.json', 'w') as outfile:
    json.dump(data, outfile)

print("Se han jugado "+str(nPartidas)+" y se han guardado data"+str(nPartidas)+".json")