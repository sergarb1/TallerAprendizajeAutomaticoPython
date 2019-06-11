#!/usr/bin/python3




#!/usr/bin/python3
#Biblioteca para clasificador arbol
from sklearn import tree
#Biblioteca para funciones del tiempo
import time
#Biblioteca para importar/exportar el modelo entrenado
import joblib
#Biblioteca generar números aleatorios
import random
#Biblioteca para realizar operaciones de sistema
import sys


#Funcion que recibe un tablero y lo pinta
def pintarTablero(tab):
    print("------------------------------------------")
    for i in range(3):
        cad=" | " +str(tab[0+(i*3)])+ " | "+str(tab[1+(i*3)])+ " | "+str(tab[2+(i*3)])+ " | "
        cad=cad.replace("0","-")
        cad=cad.replace("1","X")
        cad=cad.replace("2","O")

        print (cad)

    print("------------------------------------------")

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


#Funcion que juega la maquina y se le pasa que turno es
def jugarMaquina(turno):

    movimiento=-1
    #Lista en que se guardaran las candidatas. Estas son las que estan clasificadas como que fueron
    #jugadas victoriosas
    candidatas=[]
    for i in range(9):
        if tablero[i]==0:
            #Si no ha habido ningun movimiento, el que sea
            if movimiento==-1:
                movimiento=i
            
            #Generamos la muestra, con el estado del tablero, la posicion a la que movemos y el turno actual
            muestra=tablero + [i] + [turno]
            #Predecimos si la muestra es ganadora o no
            pred=classif.predict([muestra])
            #Si se predice como correcta, se anyade a candidatas
            if(pred[0]==1):
                candidatas.append(i)
    #Si hay candidatas, elijo una al azar
    if(len(candidatas)>0):
        movimiento=candidatas[random.randint(0,len(candidatas)-1)]
    
    tablero[movimiento]=turno
    print("Mueve la maquina a "+str(movimiento))
    return

#Funcion que juega un humano y se le pasa que turno es
def jugarHumano(turno):
    print("Elige posicion")
    num=int(input(''))
    while(num<0 or num>8 or tablero[num]!=0):
        print("Elige posicion de nuevo:")
        num=int(input(''))
    
    tablero[num]=turno
    return
        


#MAIN

#Si hay un segundo argumento, lo tomamos como el modelo a importar
if len(sys.argv)==2:
    numPart=int(sys.argv[1])
else:
#Si no se pone, elegimos 1000 por defecto
    numPart=1000


#Cargamos el clasificador
classif = joblib.load('modelTree3EnRaya'+str(numPart)+'.pkl') 

print("Partida con modelo entrenado de "+str(numPart)+" partidas")

#Incializacion de tablero
tablero=[0,0,0,0,0,0,0,0,0]
#Control del numero de jugadas
nTurnos=0;
#Eleccion de jugador 1
print("Player 1")
print("1 para jugador Humano, 2 para CPU")
num=int(input(''))

#Asignamos si es humano o CPU
if(num==2):
    player1="CPU"
else:
    player1="HUMANO"


#Eleccion de jugador 2
print("Player 2")
print("1 para jugador Humano, 2 para CPU")
num=int(input(''))

#Asignamos si es humano o CPU
if(num==2):
    player2="CPU"
else:
    player2="HUMANO"


#Mientras no haya un ganador, jugamos
while not haGanado(tablero):
    #Pintamos tablero
    pintarTablero(tablero)
    print("Esperando movimiento Player1")
    
    if(player1=="CPU"):
        # Juega la maquina, con turno 1
        jugarMaquina(1);
        pintarTablero(tablero)
        if(haGanado(tablero)):
            print("Ganador maquina Player 1")
            exit()
    else:
        #Juega humano con turno 1
        jugarHumano(1)    
        pintarTablero(tablero)
        if(haGanado(tablero)):
            print("Ganador humano Player 1")
            exit()

    #Esperamos 2 segundos para "DAR TENSION" :P
    time.sleep(2)
    
    #Sumaamos un turno
    nTurnos=nTurnos+1

    #Caso empate por turnos agotados 
    if(nTurnos==8):
        print("Empate")
        exit()
    
    print("Esperando movimiento Player2")
    time.sleep(2)

    if(player2=="CPU"):
        # Juega la maquina, con turno 2
        jugarMaquina(2);
        pintarTablero(tablero)
        if(haGanado(tablero)):
            print("Ganador maquina Player 2")
            exit()
    
    else:
        # Juega humano, con turno 2
        jugarHumano(2)    
        pintarTablero(tablero)
        if(haGanado(tablero)):
            print("Ganador humano Player 2")
            exit()
    
    nTurnos=nTurnos+1 
    #Caso empate por turnos agotados
    if(nTurnos==8):
        print("Empate")
        exit()
    

