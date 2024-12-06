

import speech_recognition as sr
import os
import win32com.client
from wikipedia import languages
import pyttsx3
import webbrowser
import openai
import datetime

# it is created by POOJA JANGID
from AppOpener import open

engine = pyttsx3.init()
engine.say("HELLO I AM AI CAN I HELP YOU PLEASE TELL ME ABOUT YOUR SEARCH")
engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold  =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return


while True:
    print("created by pooja jangid")
    print("listening...")
    query = takeCommand()
    

    #todo: take command from sites list
    sites = [["youtube", "https://www.youtube.com"], ["google", "https://www.google.com"],
             ["Facebook", "https://www.facebook.com"],
             ["wikipedia", "https://www.wikipedia.com"] ,["google chrome", "https://www.googlechrome.com"],
             ["instagram", "https://www.instagram.com"],
             ["Excel", "https://www.excel.com"]]
    for site in sites:
        if f"open {site[0]}".lower() in query.lower():
            engine.say(f"please wait i open {site[0]}  sirrr...")
            engine.runAndWait()
            webbrowser.open(site[1])
    engine.say(query)
    engine.runAndWait()


