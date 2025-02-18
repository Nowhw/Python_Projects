import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi=""

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("http://facebook.com")
    elif "open linkedln" in c.lower():
        webbrowser.open("http://linkedln.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        response = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")

        if response.status_code == 200:
            data = response.json()
            articles = data.get("articles", [])
    
            for article in articles:
                speak(article["title"])  # Print only the title
        else:
            print(f"Error: {response.status_code}, {response.text}")
        


if __name__=="__main__":
    speak("Initializing Jarvis")
    while True:
        #Listen for the wake up word jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()
    
    # recognize speech using Sphinx
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                #Listen for Command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)


                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))
