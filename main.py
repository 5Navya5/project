import pyttsx3
import requests
import speech_recognition as sr
import keyboard
import os
import subprocess as sp
import imdb
import wolframalpha
import pyautogui
import webbrowser
import time
import subprocess
import pyjokes

from datetime import datetime
from decouple import config
from random import choice
from conv import random_text
from online import find_my_ip, search_on_google, search_on_wikipedia, youtube, send_email, get_news, weather_forecast
from online import add_reminder, check_reminders
from imdb import IMDb, IMDbDataAccessError
from translate import Translator
from googletrans import Translator
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from translator import translate_text

# ...

engine = pyttsx3.init('sapi5')
engine.setProperty('volume', 1.5)
engine.setProperty('rate', 220)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

USER = config('USER')
HOSTNAME = config('BOT')

# Define the history list
history = []

def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet_me():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good morning {USER}")
        print(f"Good morning {USER}")
    elif (hour >= 12) and (hour <= 16):
        speak(f"Good afternoon {USER}")
        print(f"Good afternoon {USER}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good evening {USER}")
        print(f"Good evening {USER}")
    speak(f"I am {HOSTNAME}. How may i assist you? {USER}")
    print(f"I am {HOSTNAME}. How may i assist you? {USER}")


listening = False


def start_listening():
    global listening
    listening = True
    print("started listening ")


def pause_listening():
    global listening
    listening = False
    print("stopped listening")


keyboard.add_hotkey('ctrl+alt+k', start_listening)
keyboard.add_hotkey('ctrl+alt+p', pause_listening)


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        queri = r.recognize_google(audio, language='en-in')
        print(queri)
        if not 'stop' in queri or 'exit' in queri:
            speak(choice(random_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir,take care!")
            else:
                speak("Have a good day sir!")
            exit()

    except Exception:
        speak("Sorry I couldn't understand. Can you please repeat that?")
        queri = 'None'
    return queri



if __name__ == '__main__':
    greet_me()
    while True:
        if listening:
            query = take_command().lower()
            if "how are you" in query:
                speak("I am absolutely fine sir. What about you")
                history.append(("how are you", "I am absolutely fine sir. What about you"))

            elif "open command prompt" in query:
                speak("Opening command prompt")
                os.system('start cmd')
                history.append(("open command prompt", "Opened command prompt"))

            elif "open camera" in query:
                speak("Opening camera sir")
                sp.run('start microsoft.windows.camera:', shell=True)
                history.append(("open camera", "Opened camera"))
            

            elif "open notepad" in query:
                speak("Opening Notepad")
                subprocess.Popen('notepad')
                history.append(("open notepad", "Opened Notepad"))
            elif "open calculator" in query:
                speak("Opening calculator")
                subprocess.Popen('calc')
                history.append(("open calculator", "Opened Calculator"))
            elif "close command prompt" in query:
                speak("Closing command prompt")
                os.system('taskkill /IM cmd.exe /F')
                history.append(("close command prompt", "Closed command prompt"))

            elif "close camera" in query:
                speak("Closing camera sir")
                os.system('taskkill /IM Microsoft.Windows.Camera: /F')
                history.append(("close camera", "Closed camera"))

            elif "close notepad" in query:
                speak("Closing Notepad")
                os.system('taskkill /IM notepad.exe /F')
                history.append(("close notepad", "Closed Notepad"))

            elif "close calculator" in query:
                speak("Closing calculator")
                os.system('taskkill /IM calc.exe /F')
                history.append(("close calculator", "Closed Calculator"))
            

            elif 'set reminder' in query:
                add_reminder()
                history.append(('set reminder', 'Reminder set'))
            elif 'check reminders' in query or 'check reminder' in query or 'check my reminders' in query or 'show reminders' in query:
                check_reminders()
                history.append(('check reminders', 'Checked reminders'))

            elif 'ip address' in query:
                ip_address = find_my_ip()
                speak(
                    f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
                history.append(('ip address', f'Your IP Address is {ip_address}'))
                print(f'Your IP Address is {ip_address}')

            elif "open youtube" in query:
                speak("What do you want to play on youtube sir?")
                video = take_command().lower()
                youtube(video)
                history.append(("open youtube", f"Opened YouTube and played {video}"))

            elif "open google" in query:
                speak(f"What do you want to search on google {USER}")
                query = take_command().lower()
                search_on_google(query)
                history.append(("open google", f"Searched on Google for {query}"))
            elif "open whatsapp" in query:
                speak("Opening whatsapp")
                webbrowser.open('https://web.whatsapp.com/')
                history.append(("open whatsapp", "Opened WhatsApp"))
            elif "open instagram" in query:
                speak("Opening instagram")
                webbrowser.open('https://www.instagram.com/kamasani_charan/')
                history.append(("open instagram", "Opened Instagram"))

            elif "wikipedia" in query:
                speak("what do you want to search on wikipedia sir?")
                search = take_command().lower()
                results = search_on_wikipedia(search)
                speak(f"According to wikipedia,{results}")
                speak("I am printing in on terminal")
                print(results)
                history.append(("wikipedia", f"Searched on Wikipedia for {search}. Result: {results}"))

            # main.py


            elif "translate the following sentence from english to" in query:
                language = query.split("to")[-1].strip()
                speak("What is the sentence you want to translate?")
                text_to_translate = take_command().strip()

                # Define the model name based on the target language
                # You need to replace this with the correct model name for your target language
                model_name = f"Helsinki-NLP/opus-mt-en-fr"

                translation = translate_text(text_to_translate, model_name)
                speak(translation)
                print(f"Translated '{text_to_translate}' to {language}: {translation}")
                history.append(("translate", f"Translated '{text_to_translate}' to {language}: {translation}"))


            elif "send a mail" in query or "send an email" in query:
                    speak("On what email address do you want to send sir?. Please enter in the terminal")
                    receiver_add = input("Email address:")
                    speak("What should be the subject sir?")
                    subject = take_command().capitalize()
                    speak("What is the message ?")
                    message = take_command().capitalize()
                    if send_email(receiver_add, subject, message):
                        speak("I have sent the email sir")
                        print("I have sent the email sir")
                        history.append(("send an email", f"Sent an email to {receiver_add} with subject '{subject}' and message '{message}'"))
                    else:
                        speak("something went wrong Please check the error log")
                        history.append(("send an email", "Failed to send email"))

            elif "give me news" in query:
                speak(f"I am reading out the latest headline of today,sir")
                speak(get_news())
                speak("I am printing it on screen sir")
                print(*get_news(), sep='\n')
                history.append(("give me news", f"Read out and printed the latest news headlines"))

            elif 'weather' in query:
                ip_address = find_my_ip()
                speak("tell me the name of your city")
                city = input("Enter name of your city")
                speak(f"Getting weather report for your city {city}")
                weather, temp, feels_like = weather_forecast(city)
                speak(f"The current temperature is {temp}, but it feels like {feels_like}")
                speak(f"Also, the weather report talks about {weather}")
                speak("For your convenience, I am printing it on the screen sir.")
                print(f"Description: {weather}\nTemperature: {temp}\nFeels like: {feels_like}")
                history.append(("weather", f"Got weather report for city {city}. Description: {weather}, Temperature: {temp}, Feels like: {feels_like}"))

            # ...
            elif "tell me a joke" in query:
                
                joke = pyjokes.get_joke()
                speak(joke)
                history.append(("tell me a joke", joke))

            elif "give me movie report" in query:
                movies_db = IMDb()
                speak("Please tell me the movie name:")
                text = take_command()
                try:
                    movies = movies_db.search_movie(text)
                    speak("searching for" + text)
                    speak("I found these")
                    for movie in movies:
                        title = movie["title"]
                        year = movie.get('year', 'N/A')
                        speak(f"{title}-{year}")
                        info = movie.getID()
                        movie_info = movies_db.get_movie(info)
                        rating = movie_info.get('rating', 'N/A')
                        cast = movie_info["cast"]
                        actor = [person.get('name') for person in cast[0:5]]
                        plot = movie_info.get('plot outline', 'plot summary not available')
                        speak(f"{title} was released in {year} has imdb ratings of {rating}.It has a cast of {actor}. "
                            f"The plot summary of movie is {plot}")
                        history.append(("give me movie report", f"{title} was released in {year} has imdb ratings of {rating}.It has a cast of {actor}. The plot summary of movie is {plot}"))

                        print(f"{title} was released in {year} has imdb ratings of {rating}.\n It has a cast of {actor}. \n"
                            f"The plot summary of movie is {plot}")
                except IMDbDataAccessError:
                    speak("Sorry, I couldn't retrieve the movie information. Please try again later.")
                    history.append(("give me movie report", "Failed to retrieve movie information"))


            elif "calculate" in query:
                app_id = ""
                client = wolframalpha.Client('EGHRYJ-W326AT69QG')
                ind = query.lower().split().index("calculate")
                text = query.split()[ind + 1:]
                result = client.query(" ".join(text))
                try:
                    ans = next(result.results).text
                    speak("The answer is " + ans)
                    print("The answer is " + ans)
                    history.append(("calculate", f"Calculated result of {' '.join(text)} is {ans}"))
                except StopIteration:
                    speak("I couldn't find that . Please try again")
                    history.append(("calculate", "Failed to calculate result"))

            elif 'what is' in query or 'who is' in query or 'which is' in query:
                app_id = ""
                client = wolframalpha.Client('EGHRYJ-W326AT69QG')
                try:

                    ind = query.lower().index('what is') if 'what is' in query.lower() else \
                        query.lower().index('who is') if 'who is' in query.lower() else \
                            query.lower().index('which is') if 'which is' in query.lower() else None

                    if ind is not None:
                        text = query.split()[ind + 2:]
                        res = client.query(" ".join(text))
                        ans = next(res.results).text
                        speak("The answer is " + ans)


                        print("The answer is " + ans)
                        history.append(("what is/who is/which is", f"Answered query {' '.join(text)} with {ans}"))
                    else:
                        speak("I couldn't find that. Please try again.")
                        history.append(("what is/who is/which is", "Failed to answer query"))
                except StopIteration:
                    speak("I couldn't find that. Please try again.")
                    history.append(("what is/who is/which is", "Failed to answer query"))

            elif "give me the previous task" in query:
                if history:
                    last_task, last_result = history[-1]
                    speak(f"The last task you asked me was '{last_task}'. The result was '{last_result}'")
                    print(f"The last task you asked me was '{last_task}'. The result was '{last_result}'")
                else:
                    speak("There are no previous tasks.")
                                
            elif "exit" in query or "quit" in query:
                    speak("Goodbye!")
                    break
            