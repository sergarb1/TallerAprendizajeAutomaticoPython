#!/usr/bin/python3



#sudo apt-get install python3-pyaudio pavucontrol
#pip3 install SpeechRecognition pyaudio
import speech_recognition as sr
import webbrowser


reconocedor = sr.Recognizer()
#print(sr.Microphone.list_microphone_names())
with sr.Microphone() as entradasVoz:
    print("Por favor, hable ahora y diga que quiere buscar en Youtube")
    escuchando = reconocedor.listen(entradasVoz)
    print("Analizando...")
    try:
        fraseReconocida=reconocedor.recognize_google(escuchando,language = "es-ES")
        print("Dijiste: "+fraseReconocida)
        webbrowser.open('https://www.youtube.com/results?search_query='+fraseReconocida)

 
    except:
         print("Por favor, hable de nuevo")