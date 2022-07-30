import pyttsx3 # To get a voice 
import datetime
import wikipedia
import speech_recognition as sp # To recognise a voice data
import webbrowser # For opening links
import os # For UI Intraction
import pyjokes # For jokes
from playsound import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# change value 0 for men and 1 for women



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning")
        speak("Good Morning!")

    if hour>=12 and hour<18:
        print("Good Afternoon")
        speak("Good Afternoon!")
        
    if hour>=18 and hour<24:
        print("Good Evening")
        speak("Good Evening!")



def wishMe():
    if a==1:
        print("Welcome Sir,")
        speak("Welcome Sir , the system will be started in few more seconds")
        
def takeCommand():

    r = sp.Recognizer()
    with sp.Microphone() as source:
        print("Speak Now ... ")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Please wait ...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

        
       

    except Exception as e:   
        print("Sorry i didn't get it , say that again please ") 
        speak("Sorry i didn't get it , say that again please")
        return "None"
    return query

    

if __name__ == "__main__":
    greetings()
    wishMe()
    while True:
        query = takeCommand().lower()
        

        # Created logics based on words inside a query and putting it into a loop 
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak('Ok sir , here we go')

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak('Ok sir , here we go')

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak('Ok sir , here we go') 

        elif 'hello' in query:
            speak('Oh Hello Sir')
            joke=pyjokes.get_joke(language="en" , category="neutral")
            speak(joke)

        
        elif 'how are you' in query:
            speak('I am fine Sir')

        elif 'alarm' in query:
            alhr=int(input('Hour'))
            almn=int(input('Minute'))

        elif 'open instagram' in query:
            webbrowser.open('instagram.com')
            speak('Ok sir , here we go')

        elif 'open gmail' in query:
            webbrowser.open('gmail.com')
            speak('Ok sir , here we go')
            speak('Looks Like Spammers really like you')

        elif 'thank' in query:
            speak('Well, Welcome')

        

        elif 'play music' in query:
            speak("Playing some music now ")
            playsound('starboy.mp3')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\Program Files\Microsoft VS Code\code.exe"
            os.startfile(codePath)
            speak("Opening Visual Studio Code")

        elif "try" in query:
            with open("data.txt") as word_file:
                words = word_file.read()
                speak(words)


        elif 'stop' in query:
            speak('Ok No Problem')
            print('----------------------------DEVELOPED BY YATHARTH-------------------------------------')
            print('GOOD BYE')
            break

        elif 'joke' in query :
            joke=pyjokes.get_joke(language="en" , category="neutral")
            speak(joke)
