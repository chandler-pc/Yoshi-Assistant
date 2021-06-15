import os
import time
import datetime
import requests
import webbrowser
import subprocess
import pyttsx3
import speech_recognition as sr
import dotenv
import wikipedia
import pypresence

# init
dotenv.load_dotenv()
wikipedia.set_lang('es')

# discord presence
RPC = pypresence.Presence(os.getenv('DISCORD_CLIENT_ID'))
RPC.connect()
RPC.update(state='Yoshino :D', large_image='yoshifull', details='Ni pe2 taba aburrido.')

# config pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


def speak(txt):
    engine.say(txt)
    engine.runAndWait()


# config speechrecognition
def listen(name):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(name)
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio, language='es-US')
            print(f"Escuché : {command}\n")
        except sr.UnknownValueError:
            print("No entendí.")
            return ""
        except sr.RequestError as e:
            speak("Sin servicio de Google.")
            print(e)

            return ""
        return command.lower()


# config main function
if __name__ == '__main__':
    while 1:
        if datetime.datetime.now().minute == 0:
            subprocess.run(['python', 'D:/Archivos/yoshi/anotherComms/clase.py'])
        comm = listen('Esperando Activación...')
        if 'yoshino' in comm:
            print('Palabra clave dicha...')
            if 'fuera' in comm:
                speak('Apagando a Yochi...')
                exit()
            elif 'navegador' in comm or 'buscador' in comm or 'google' in comm:
                speak('Abriendo Google...')
                webbrowser.open_new_tab('www.google.com')
            elif 'youtube' in comm:
                speak('Abriendo Youtube...')
                webbrowser.open_new_tab('www.youtube.com')
            elif 'apag' in comm or 'apág' in comm:
                speak("¿Seguro que quieres apagar la computadora?")
                conf = listen('Esperando Confirmación : Sí/No')
                if 'si' in conf or 'afirmativo' in conf or 'sí' in conf:
                    time.sleep(5)
                    subprocess.call(["shutdown", "-s"])
                    exit()
                else:
                    speak('No se apagará la computadora.')
            elif 'clase' in comm:
                subprocess.run(['python', 'D:/Archivos/yoshi/anotherComms/clase.py'])
            elif 'hora' in comm:
                speak('Son las {} horas con {} minutos'.format(datetime.datetime.now().strftime("%H"),
                                                               datetime.datetime.now().strftime("%M")))
            elif 'tiempo' in comm or 'clima' in comm or 'temp' in comm:
                # https://www.weatherapi.com/
                # Speak('¿De dónde quieres saber el clima?')
                # location = Listen('Esperando locación...').replace(" ","_")
                weather = requests.get(
                    'http://api.weatherapi.com/v1/current.json?key={}&q={}&lang=es'.format(os.getenv('WEATHER_API'),
                                                                                           'Lima')).json()
                speak('El clima es ' + weather['current']['condition']['text'] + ' y la temperatura es ' + str(
                    weather['current']['temp_c']))
            elif 'ipedia' in comm:
                speak('¿Qué quieres buscar en Wikipedia?')
                search_keys = listen('Esperando valores...')
                speak(wikipedia.summary(search_keys, sentences=2))
