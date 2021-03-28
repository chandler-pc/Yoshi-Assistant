import pyttsx3
import speech_recognition as sr
import webbrowser
import subprocess
import time
import datetime

#config pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)

def Speak(txt):
    engine.say(txt)
    engine.runAndWait()

#config speechrecognition
def Listen(name):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(name)
        r.adjust_for_ambient_noise(source) 
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio, language='es-US')
            print(f"Escuché : {command}\n")
        except sr.UnknownValueError:
            Speak("No entendí.")
            return "None"
        except sr.RequestError as e:
            Speak("Sin servicio de Google.")
            print(e)
            return "None"
        return command.lower()

#config main function
if __name__=='__main__':
    while 1:
        ok = Listen('Esperando Activación...')
        if 'yoshi' in ok:
            print('Palabra clave dicha...')
            Speak('¿Cómo puedo ayudarte?')
            comm = Listen('Esperando Comando...')
            if 'fuera' in comm:
                Speak('Apagando a Yochi...')
                exit()
            elif 'cancel' in comm:
                Speak('Activación Cancelada...')
            elif 'navegador' in comm or 'buscador' in comm or 'google' in comm:
                Speak('Abriendo Google...')
                webbrowser.open_new_tab('www.google.com')
            elif 'youtube' in comm:
                Speak('Abriendo Youtube...')
                webbrowser.open_new_tab('www.youtube.com')
            elif 'apag' in comm or 'apág' in comm:
                Speak("¿Seguro que quieres apagar la computadora?")
                conf = Listen('Esperando Confirmación : Sí/No')
                if 'si' in conf or 'afirmativo' in conf or 'sí' in conf:
                    time.sleep(5)
                    subprocess.call(["shutdown", "-s"])
                    exit()
                else:
                    Speak('No se apagará la computadora.')
            elif 'hora' in comm:
                Speak('Son las {} horas con {} minutos'.format(datetime.datetime.now().strftime("%H"),datetime.datetime.now().strftime("%M")))
            

