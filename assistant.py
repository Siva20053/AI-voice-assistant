import datetime
import time
import os
import sys
import webbrowser
import keyboard
import pyttsx3
import psutil
import speech_recognition as sr
import pyautogui
import json
import joblib
import numpy as np

with open("AI assistant/intents.json" , "r") as f:
    data = json.load(f)

model = joblib.load("AI assistant/intent_classifier.pkl")
le = joblib.load("AI assistant/label_encoder.pkl")


def initialize_engine():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-60)
    volume = engine.getProperty('volume')
    engine.setProperty('volume',volume+0.25)
    return engine

def speak(text):
    engine = initialize_engine()
    engine.say(text)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening....",end="",flush=True)
        r.pause_threshold = 1.0
        r.phrase_threshold = 0.3
        r.sample_rate = 48000
        r.dynamic_energy_threshold = True
        r.operation_timeout = 5
        r.non_speaking_duration = 0.5
        r.dynamic_energy_adjustment = 2
        r.energy_threshold = 4000
        r.phrase_time_limit = 10
        audio = r.listen(source)
    try:
        print('\r',end="",flush=True)
        print("Recognizing....",end="",flush=True)
        query = r.recognize_google(audio , language = 'en-in')
        print('\r',end="",flush=True)
        print(f"User said : {query}\n")
    except Exception as e:
        speak("Say that again please")
        return "None"
    return query

def cal_day():
    day = datetime.datetime.today().weekday()+1
    day_dict={
    1:"Monday",
    2:"Tuesday",
    3:"Wednesday",
    4:"Thursday",
    5:"Friday",
    6:"Saturday",
    7:"Sunday",
    }
    if day in day_dict.keys():
       week_day=day_dict[day]
    return week_day

def wish_me():
    hour = int(datetime.datetime.now().hour)
    t = time.strftime("%I:%M:%p")
    day = cal_day()
    if (hour >= 0) and (hour <= 12) and ("AM" in t):
        speak(f"Good Morning,Siva ! it's {day} and time is {t}")
    elif (hour >= 12) and (hour <= 16) and ("PM" in t):
        speak(f"Good Afternoon,Siva ! it's {day} and time is {t}")
    else:
        speak(f"Good Evening,Siva ! it's {day} and time is {t}")
    speak("NAMI,at your service..." \
    "What can I do for you...")


def social_media(command):
    if 'instagram' in command:
        speak("Opening instagram")
        webbrowser.open("https://www.instagram.com/")
    elif 'facebook' in command:
        speak("Opening facebook")
        webbrowser.open("https://www.facebook.com/")
    elif 'youtube' in command:
        speak("Opening youtube")
        webbrowser.open("https://www.youtube.com/")
    elif 'whatsapp' in command:
        speak("Opening whatsapp")
        webbrowser.open("https://web.whatsapp.com/")

def open_app(command):
    if 'calculator' in command:
        speak('opening calculator')
        os.startfile('C:\\Windows\\System32\\calc.exe')
    elif 'notepad' in command:
        speak('opening notepad')
        os.startfile('C:\\Windows\\System32\\notepad.exe')

def close_app(command):
    if 'calculator' in command:
        speak('Closing calculator')
        os.system("taskkill /f /im calc.exe")
    elif 'notepad' in command:
        speak('Closing notepad')
        os.system("taskkill /f /im notepad.exe")
#def open_anyapp(command):
    #app_name = command.replace("open","").strip()
    #os.system(f"start {app_name}")

def browse_google(query):
    if 'google' in query:
        speak("Boss,what should I search for....")
        s = command().lower()
        webbrowser.open(f"{s}")

def battery_percent():
    battery = psutil.sensors_battery()
    percentage = battery.percent
    speak(f"Siva , your system's battery is at {percentage}percent")


if __name__ == "__main__" :
    wish_me()
    while True:
        query = command().lower()
        #query = input("Enter the query-->")
        #open_anyapp(query)

        if ('instagram' in query) or ('facebook' in query) or ('whatsapp' in query) or ('youtube' in query):
            social_media(query)
        elif ('volume down' in query) or ('decrease volume' in query):
            pyautogui.press('volumedown')
            speak('Volume decreased')
        elif ('volume up' in query) or ('increase volume' in query):
            pyautogui.press('volumeup')
            speak('Volume increased')
        elif ('volume mute' in query) or ('mute volume' in query):
            pyautogui.press('volumemute')
            speak('Volume muted')
        elif ('open calculator' in query) or ('open notepad' in query):
            open_app(query)
        elif ('close calculator' in query) or ('close notepad' in query):
            close_app(query)
        elif ('who' in query) or ('what' in query) or ('when' in query) or ('how' in query) or ('hi' in query) or ('hello' in query) or ('idiot' in query) or ('thanks' in query) or ('bye' in query) or ('joke' in query) or ('funny' in query) or ('age' in query):
            result = model.predict([query])
            tag = le.inverse_transform([result])
            for i in data["intents"]:
                if i["tag"] == tag :
                    speak(np.random.choice(i["responses"]))
        elif ('open google' in query):
            browse_google(query)
        elif ("battery" in query):
            battery_percent()
        elif ("sign off" in query) or ("sign of" in query) or ("exit" in query) or ("log out" in query):
            speak("bye Siva, see you later!")
            sys.exit()
