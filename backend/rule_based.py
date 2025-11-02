
import os
import sys
import webbrowser
import pyautogui
import psutil
def social_media(command):
    if 'instagram' in command:
        webbrowser.open("https://www.instagram.com/")
        return("Opening instagram")
    elif 'facebook' in command:
        webbrowser.open("https://www.facebook.com/")
        return("Opening facebook")
    elif 'youtube' in command:
        webbrowser.open("https://www.youtube.com/")
        return("Opening youtube")
    elif 'whatsapp' in command:
        webbrowser.open("https://web.whatsapp.com/")
        return("Opening whatsapp")

def open_app(command):
    if 'calculator' in command:
        os.startfile('C:\\Windows\\System32\\calc.exe')
        return('opening calculator')
    elif 'notepad' in command:
        os.startfile('C:\\Windows\\System32\\notepad.exe')
        return('opening notepad')

def close_app(command):
    if 'calculator' in command:
        os.system("taskkill /f /im calc.exe")
        return('Closing calculator')
    elif 'notepad' in command:
        os.system("taskkill /f /im notepad.exe")
        return('Closing notepad')


def browse_google(query):
    if 'google' in query:
        s = query().lower()
        webbrowser.open(f"{s}")
        return(f"Boss,showing results for {s}")

def battery_percent():
    battery = psutil.sensors_battery()
    percentage = battery.percent
    return(f"Siva , your system's battery is at {percentage}percent")

def handle_rule_based(query):
    query = query.lower()
    if ('instagram' in query) or ('facebook' in query) or ('whatsapp' in query) or ('youtube' in query):
            social_media(query)
    elif ('volume down' in query) or ('decrease volume' in query):
            pyautogui.press('volumedown')
    elif ('volume up' in query) or ('increase volume' in query):
            pyautogui.press('volumeup')
    elif ('volume mute' in query) or ('mute volume' in query):
            pyautogui.press('volumemute')
    elif ('open calculator' in query) or ('open notepad' in query):
            open_app(query)
    elif ('close calculator' in query) or ('close notepad' in query):
            close_app(query)
    elif ('open google' in query):
            browse_google(query)
    elif ("battery" in query):
            battery_percent()
    elif ("sign off" in query) or ("sign of" in query) or ("exit" in query) or ("log out" in query):
            print("bye Siva, see you later!")
            sys.exit()
    else:
          return None