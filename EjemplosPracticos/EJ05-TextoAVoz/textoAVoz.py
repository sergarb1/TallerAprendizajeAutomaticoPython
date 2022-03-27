#!/usr/bin/python3

#pip3 install gtts
#sudo apt install mpg321
from gtts import gTTS
import os
tts = gTTS('Van dos tomates y uno dice ay va, que frio hace. Y el otro responde: ay va, un tomate que habla', lang='es-ES')

with open("tmp.mp3", "wb") as archivo:
    tts.write_to_fp(archivo)
os.system("mpg321 tmp.mp3")


















'''
#pip3 install pyttsx3
#sudo apt install espeak
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 120)
engine.setProperty('voice', 'spanish')
engine.setProperty('volume', 1)


# It's just a text to speech function..
def saySomething(somethingToSay):
    engine.say(somethingToSay)
    engine.runAndWait()


while True:
    something = input("Something to say? ")
    print("Saying something with speakers..")
    saySomething(something)

'''