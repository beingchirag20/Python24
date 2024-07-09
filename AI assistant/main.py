import speech_recognition as sr
import pyttsx3
import webbrowser
import requests

rec = sr.Recognizer()
engine = pyttsx3.init()
newsAPI = "9af21f97b7b2495e813b21d9d67cdd61"


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  

rate = engine.getProperty('rate')
engine.setProperty('rate', 150)  


def speak(text):
    engine.say(text)
    engine.runAndWait()

      
name = str(input("Enter your name:"))
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    if "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")

    if "open github" in c.lower():
        webbrowser.open("https://github.com/")

    if "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/login/")

    if "news" in c.lower():
        r = requests.get(
"https://newsapi.org/v2/top-headlines?country=in&apiKey=9af21f97b7b2495e813b21d9d67cdd61")
        if r.status_code == 200:
            data = r.json()

            articles = data.get('articles', [])

            for article in articles:
                speak(article['title'])
    
        
if __name__ == "__main__":
    speak("Welcome sir...")
    while True:
        r = sr.Recognizer()
        print("Recognizing..")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "rolex"):
                speak(f"Hello {name} sir")
                #Listen for command
                with sr.Microphone() as source:
                    speak("rolex Activated...")
                    print("rolex Activated...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)                
        except Exception as e:
            print("Error;{0}".format(e))
