import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import smtplib

#set up speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
name = 'Dan'

#will pronounce the parameter
def speak(text):
    engine.say(text)
    engine.runAndWait()

#greets user based on time of day and collects users name 
def greeting():
    ## This code block takes users name from microphone and replaces the hardcoded 'name' variable
    # speak("Hello, My name is Jarvis, what is your name?")
    # r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     audio = r.listen(source)
    # try: 
    #     name = r.recognize_google(audio, language = 'en-us')
    # except Exception as e:
    #     speak("I didnt recongsie that, what is your name?")

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good Morning {name}, How can I help you today?")

    elif hour >=12 and hour < 18:
        speak(f"Good Afternoon {name}, How can I help you today?")

    else:
        speak(f"Good Evening {name}, How can I help you today?")

#takes commands from microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language = 'en-us')
    except Exception as e:
        speak("I did not understand,Say that again Please")
        query = None

    return query


#runs on programme start
greeting()
query = takeCommand()


#Logic for basic tasks from the query
if 'wikipedia' in query.lower():
    speak("Searching Wikipedia")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences = 1)
    speak(results)

elif 'time' in query.lower():
    time = datetime.datetime.now().strftime("%H:%M")
    speak(f"the time is {time}")

elif 'list' in query.lower():
    os.system("ls")

elif 'new' in query.lower():
    os.system("git init")
    speak("New repository created")

elif 'add' in query.lower():
    os.system("git add .")

elif 'commit' in query.lower():
    speak("Commit messaage please")
    message = takeCommand()
    os.system("git commit -m {message}")

elif 'push' in query.lower():
    os.system("git push")

elif 'status' in query.lower():
    os.system("git status")

elif 'checkout' in query.lower():
    speak("Which branch should I checkout?")
    branch = takeCommand()
    os.system(f"git checkout {branch}")

elif 'new branch' in query.lower():
    speak("What name shopud I give the new branch?")
    branch = takeCommand()
    os.system(f"git checkout -b {branch}")

elif 'list branch' in query.lower():
    os.system(f"git branch")

elif 'pull' in query.lower():
    os.system("git pull")

elif 'merge' in query.lower():
    speak("What branch should I merge?")
    branch = takeCommand()
    os.system(f"git merge {branch}")