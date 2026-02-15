import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import playlist
import os

recognizer=sr.Recognizer()

def ask_jarvis(prompt, max_tokens=200):
    api_key = os.getenv("GEMINI_API_KEY")
    MODEL_NAME = "gemini-2.5-flash"
    url = f"https://generativelanguage.googleapis.com/v1/models/{MODEL_NAME}:generateContent"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ],
        "generationConfig": {
            "maxOutputTokens": max_tokens
        }
    }

    response = requests.post(url + f"?key={api_key}", headers=headers, json=data)

    try:
        res_json = response.json()
        return res_json["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        print("Error in Gemini response:", e, response.text)
        return "Sorry, I couldn't get an answer."

def get_news():
    api_key=os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/everything?q=India&sortBy=publishedAt&apiKey={api_key}"

    response = requests.get(url).json()
    if response.get("status") == "ok":
        articles = response.get("articles")
        news_list = [article["title"] for article in articles]
        return news_list
    else:
        print("Error from API:", response.get("message"))
        return []

def speak(text):
    print("Jarvis:",text)
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    print("Processing:",c)
    if "open google" in c.lower():
        speak("opening google")
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        speak("opening facebook")
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        speak("opening youtube")
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        speak("opening linkedin")
        webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=playlist.music[song]
        speak(f"Playing {song}")
        webbrowser.open(link)

    elif "news" in c.lower():
        headlines=get_news()
        if headlines:
            speak("Top Headlines in India for today:")
            for i in headlines[:5]:
                speak(i)
            speak("Thank You!")
        else:
            speak("Sorry for the inconvinience!!!No headlines for today")

    elif "bye" in c.lower() or "stop" in c.lower():
        speak("Bye")
        exit()
    
    else:
        answer=ask_jarvis(c)
        speak(answer)

if __name__=="__main__":
    speak("Initializing Jarvis....")
    r=sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio=r.listen(source,timeout=8,phrase_time_limit=8)
            print("Recognizing...")
            word=r.recognize_google(audio)

            if 'jarvis' in word.lower():
                print("Speaking now...")
                speak("hello!This is Jarvis")
                print("Jarvis Activated....")

                with sr.Microphone() as source:
                    audio=r.listen(source)
                    command=r.recognize_google(audio)
                processCommand(command)

        except sr.WaitTimeoutError:
            print("No speech detected, continuing...")
        except sr.UnknownValueError:
            print("Could not understand speech - try speaking louder and clearer")
        except sr.RequestError as e:
            print(f"Network error: {e}")
            speak("Network connection issue")
        except Exception as e:
            print(f"Error: {type(e).__name__}: {e}")
            if str(e) == "":
                print("Empty error - likely microphone or network issue")
                speak("There seems to be a microphone or connection issue")