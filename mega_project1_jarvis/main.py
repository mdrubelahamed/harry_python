import webbrowser
import pyttsx3
import speech_recognition as sr
import music_library
import website_library
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
api_key = "3583ef69bb974afa8bf0837ad189bc8b"

# speak what the text he will get
def speak(text):
    engine.say(text)
    engine.runAndWait()


# it will process the command and find if any command can get executed
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    # play music
    elif c.lower().startswith("play"):
        word = c.lower().split(" ")[1]
        if word in music_library.music:
            link = music_library.music[word]
            webbrowser.open(link)
    
    # open websites
    elif c.lower().startswith("open"):
        website = c.lower().split(" ")[1]
        if website in website_library.websites:
            link = website_library.websites[website]
            webbrowser.open(link)

    # get news
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])


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

