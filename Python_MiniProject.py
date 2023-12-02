import speech_recognition as sr
import pyttsx3
import pyaudio
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys

Listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text) :
    engine.say(text)
    engine.runAndWait()

def take_command() :
    try :
         with sr.Microphone() as source :
            print("Listening ...... ")
            voice = Listener.listen(source)
            command = Listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command :
                commad = command.replace('alexa', '')
                print(command)
    except :
      pass
    return command

def run_alexa() :
    command = take_command()
    print(command)
    if 'play a song' in command :
        song = 'Arijit Singh'
        talk('Playing Some Music. ')
        print('Playing..... ')
        pywhatkit.playonyt(song)
    elif 'play' in command :
        song = command.replace('play', '')
        talk('Playing ' + song)
        print('Playing.....')
        pywhatkit.playonyt(song)
    elif 'time' in command :
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current Time is ' + time )
    elif 'who the heck is' in command :
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command :
        get_j = pyjokes.get_joke()
        print(get_j)
        talk(get_j)
    elif 'date' in command :
        talk('Sorry, I have Headache. ')
    elif 'are you single' in command :
        talk('No, I am in a Relationship with Wifi. ')
    elif 'stop' in command :
        talk('Good Bye. ')
        sys.exit()
    else :
        talk('Please Say the Command Again. ')

while True :
    run_alexa()


