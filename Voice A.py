
import speech_recognition as sr
import pyttsx3 as p
import webbrowser
import subprocess
import time

def record_audio(ask=False):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
            Grizzly_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            Grizzly_speak('sorry didnt get that ')
        except sr.RequestError:
            Grizzly_speak('Sorry, my speech service is down')
        return voice_data


def Grizzly_speak(audio_string):
    engine=p.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(audio_string)
    print(audio_string)
    engine.runAndWait()


def open(voice_data):
        if'open fortnite'in voice_data:
            subprocess.call('E://Games//Fortnite//FortniteGame//Binaries//Win64//FortniteClient-Win64-Shipping.exe')
            Grizzly_speak('To call me back press F8 and say grizzly')
            exit()
        if'open Discord'in voice_data:
            subprocess.call('C://Users//asamo//AppData//Local//Discord//app-1.0.9002//Discord.exe')
            Grizzly_speak('To call me back press F8 and say grizzly')
            exit()
        if'open YouTube'in voice_data:
            webbrowser.open("https://www.youtube.com/")
            Grizzly_speak('To call me back press F10 and say grizzly')
            exit()
        if 'open Spotify'in voice_data:
            subprocess.call('C://Users//asamo//AppData//Roaming//Spotify//Spotify.exe')
            Grizzly_speak('To call me back press F10 and say grizzly')
            exit()
        if'open Apex'in voice_data:
            subprocess.call('E://steam//steamapps//common//Apex Legends//r5apex.exe')

        if 'open Steam'in voice_data:
            subprocess.call('E://steam//steam.exe')
            Grizzly_speak('To call me back press F10 and say grizzly')
            exit()

def respond(voice_data):
        print(voice_data)
        if 'grizzly' in voice_data:
            Grizzly_speak('how can I help you')
        if 'what is your name' in voice_data:
            Grizzly_speak('My name is Grizzly')
        if 'what time is it' in voice_data:
            Grizzly_speak(time.ctime())
        if 'exit' in voice_data:
            Grizzly_speak("To Call me back press f8 and say Grizzly")
            exit()
        if'who is your creator' in voice_data:
            Grizzly_speak('my creator is the best, he is so sexy, his name is john williams Asamoah')
        if'how are you'in voice_data:
            Grizzly_speak('am good , I have just been taking a long nap')


def search(voice_data):
    if 'search' in voice_data:
        search = record_audio('what do you want to search for? ')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        Grizzly_speak('Here is what I found for ' + search)
    if 'Sy' in voice_data:
        search2 = record_audio('what do you want to search on youtube? ')
        url = 'https://youtube.com/search?q=' + search2
        webbrowser.get().open(url)
        Grizzly_speak('Here is what I found for' + search2)

    if 'find location' in voice_data:
        location = record_audio('what is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)








while 1:
    voice_data = record_audio()
    respond(voice_data)
    search(voice_data)
    open(voice_data)

    if 'thank you' in voice_data:
        break
