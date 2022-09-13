import pyttsx3
from googlesearch import search
import pywhatkit 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
from time import strftime
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetme():
    hour = int(datetime.datetime.now().hour)
    if(hour < 12 and hour > 5):
        speak('good morning Aashu')
    if(hour > 12 and hour < 18):
        speak('Good afternoon Aashu')
    if(hour > 18 and hour < 21):
        speak('good evening Aashu')


def tkcmd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('recognizing')
        query = r.recognize_google(audio, language='en-in')
        print(query)
        return query
    except Exception as e:
        print('I didnt understand please repeat')
        return 'None'


if(__name__ == '__main__'):
    greetme()
    while(True):
        query = tkcmd().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences = 3)
            speak('according to wikipedia')
            print(results)
            speak(results)

        if 'youtube' in query:
            speak('opening in youtube')
            query = query.replace('youtube','')
            pywhatkit.playonyt(query)
            print(query)
        
        if 'google' in query:
            speak('searching google')
            query = query.replace('google','')
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:/Program Files/Google/Chrome/Application/chrome.exe"))
            
            for j in search(query, tld="co.in", num=1, stop=1, pause=2): webbrowser.get('chrome').open(j)
            print(query)
            
