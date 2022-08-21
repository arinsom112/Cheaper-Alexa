import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)   
engine.say(' What can i do for you?')
engine.runAndWait()       

def talk(text):
    engine.say(text)                     
    engine.runAndWait()

def take_command():
    try: 
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', ' ')
                print(command)       
    except:
        pass

    return command

def run_alexa():
    command = take_command()
    song = command.replace('play', '')
    if "play" in command:
        talk('playing' + song)
        print('now playing: ', song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("It is " + time)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk("Here's a joke for you.. " + joke)
    else:
        talk('Can you please repeat again? ')

run_alexa()