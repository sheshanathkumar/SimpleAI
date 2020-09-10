import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

from click import File

f = open("converation.txt", "a")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # using ZIRA Voice


def speak(audio):
    '''Take audio and play it'''
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    '''Listening to user through microphone'''
    r = sr.Recognizer()
    # print(sr.Microphone.list_microphone_names())
    #file to store all conversation
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, timeout=3)
        try:
            print('Recognizing....')
            query = r.recognize_google(audio, language='en-in')
            f.write( f"{datetime.datetime.now()} user asked->  {query} \n")
            print(f"user said->  {query}")
        except Exception as e:
            print(e)
            speak("Say that again please...")
            f.write(f"{datetime.datetime.now()} Aditi Requested:- Say that again please... \n")
            f.write(f"{datetime.datetime.now()} Aditi Replied:- Nothing detected \n")
            f.close()
            return "None"
        f.close()
        return query


def startAI():
    '''Start up voice for this AI'''
    speak("Hello Sir!  ")
    f.write(f"{datetime.datetime.now()} Aditi Activated\n")
    f.write(f"{datetime.datetime.now()} Aditi Replied-> Hello Sir\n")
    hour = (datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak(f"Good Morning ! ")
    elif 12 <= hour <= 4:
        speak(f"Good AfterNoon  !")
    else:
        speak(f"Good Evening!")
    speak("I am your Navigator! How may I assist you? ")


def checkWikipediya (speech):
    speak("looking into wikipedia...")
    f.write(f"{datetime.datetime.now()} Aditi Replied-> looking into wikipedia...\n")
    speech = speech.replace("wikipedia", "")
    result = wikipedia.summary(speech, sentences=2)
    speak("Wikipedia says :-  ")
    print(result)
    f.write(f"{datetime.datetime.now()} Aditi Replied-> {result}\n")
    speak(result)


if __name__ == '__main__':
    startAI()
    speech = takeCommand().lower();
    #########Keywords###########
    keys = ['search', 'what', 'who', 'wikipediya']
    deny = ['no', 'quit']
    stackoverflow = ['stack', 'overflow']
    while True:

        if any(x in speech for x in keys):
            checkWikipediya(speech)

        elif 'youtube' in speech:
            speak("Opening Youtube.com")
            f.write(f"{datetime.datetime.now()} Aditi Replied-> Opening Youtube....\n")
            webbrowser.open("www.youtube.com")

        elif 'google' in speech:
            speak("Opening Google.com")
            f.write(f"{datetime.datetime.now()} Aditi Replied-> Opening Google....\n")
            webbrowser.open("www.google.com")

        elif any( x in speech for x in stackoverflow) :
            speak("Opening Stackoverflow.com")
            f.write(f"{datetime.datetime.now()} Aditi Replied-> Opening StackOverFlow....\n")
            webbrowser.open("www.stackoverflow.com")

        elif 'play music' in speech:
            music_dir = "C:\\Users\\HOME\\Music";
            songs = os.listdir(music_dir);
            print (f"playing current song -> {songs[0]}")
            f.write(f"{datetime.datetime.now()} Aditi Played-> {songs[0]}\n")
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'none' in speech:
            print("nothing detected")
            speech = takeCommand().lower()

        speak("any more help I can do Sir-> ")
        f.write(f"{datetime.datetime.now()} Aditi Asked-> Any more help I can do Sir\n")
        speech = takeCommand().lower()

        if any(x in speech for x in deny) :
            speak("Thank you! Bye")
            f.write(f"{datetime.datetime.now()} Aditi Deactivated\n")
            break;
        else:
            continue
