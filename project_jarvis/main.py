import os
import webbrowser
import pyttsx3
import speech_recognition as sr
import music_library
import website_library
import requests
import pygame
from dotenv import load_dotenv
from gtts import gTTS

recognizer = sr.Recognizer()
engine = pyttsx3.init()

load_dotenv()  # loads from .env
api_key = os.getenv("API_KEY")

# speak what the text he will get
def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3") 


# it will process the command and find if any command can get executed
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif c.lower().startswith("play"):
        word = c.lower().split(" ")[1]
        if word in music_library.music:
            link = music_library.music[word]
            webbrowser.open(link)

    elif c.lower().startswith("open"):
        website = c.lower().split(" ")[1]
        if website in website_library.websites:
            link = website_library.websites[website]
            webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}")
        print(r)
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
    else:
        # add openai key, not added right now because of some banking problem will add later
        pass

# start main 
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    print("Listening for wake word...")

    # keep asking for the wake word until it get for activation
    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=1)  # Adjust timeout
            word = recognizer.recognize_google(audio)
            # print(word)
            if "jarvis" in word.lower():
                speak("Yes, Mr. Rex.")
                break
        except sr.UnknownValueError:
            print("Didn't quite catch that. Please try again.")
        except sr.RequestError as e:
            print(f"Error: {e}")

    # after activation find for command which can get executed
    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
                print("Listening for command...")
                audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print(command)
            processCommand(command)

        except sr.UnknownValueError:
            print("Didn't quite catch that. Please try again.")
        except sr.RequestError as e:
            print(f"Error: {e}")

