import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config
import pyttsx3
import datetime
import time
from commands import take_command
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



EMAIL = ""
PASSWORD = ""

reminders = []


def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]


def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results


def search_on_google(query):
    kit.search(query)


def youtube(video):
    kit.playonyt(video)


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(receiver_address, subject, message):
    try:
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = 'navyachowdary428@gmail.com'
        message['To'] = receiver_address
        message['Subject'] = subject

        # The body and the attachments for the mail
        message.attach(MIMEText(message, 'plain'))

        # Use gmail with port
        session = smtplib.SMTP('smtp.gmail.com', 587)

        # Enable security
        session.starttls()

        # Login with mail_id and password
        session.login('navyachowdary428@gmail.com', 'navya@2003')

        text = message.as_string()
        session.sendmail('your_email_address', receiver_address, text)
        session.quit()
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def get_news():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=0a308e7734eb476c831d677afe959949"
    response = requests.get(url)
    result = response.json()
    headlines = []
    if result["status"] == "ok":
        articles = result["articles"]
        for article in articles[:5]:  # limit to the first 5 articles
            headlines.append(article["title"])  # add the title of the article to the list
    else:
        print(result)  # print the error message if the API request fails
    return headlines  # return the list of headlines


def weather_forecast(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=17b69427a67880529f07cbac0a7b0150&units=metric"
    response = requests.get(url)
    res = response.json()
    if response.status_code == 200 and 'weather' in res:
        weather = res["weather"][0]["main"]
        temp = res["main"]["temp"]
        feels_like = res["main"]["feels_like"]
        return weather, temp, feels_like
    else:
        print(f"Error: {res['message']}")  # print the error message if the API request fails
        return None, None, None



def add_reminder():
    speak("What is the reminder?")
    reminder = take_command()
    speak("When should I remind you? Please tell me the time in the format 'hour:minute AM/PM'")
    time_str = take_command()
    time_str = time_str.replace('a.m.', 'AM').replace('p.m.', 'PM')
    now = datetime.datetime.now()
    time_obj = datetime.datetime.strptime(time_str, '%I:%M %p')
    reminder_time = now.replace(hour=time_obj.hour, minute=time_obj.minute, second=0, microsecond=0)
    reminders.append((reminder_time, reminder))
    speak("Reminder set")

def check_reminders():
    now = datetime.datetime.now()
    for reminder in reminders.copy():
        if reminder[0] <= now:
            print(f"Reminder: {reminder[1]}")  # Print reminder to console
            speak(f"Reminder: {reminder[1]}")
            reminders.remove(reminder)
    # Remove reminders for past days
    reminders[:] = [reminder for reminder in reminders if reminder[0].date() == now.date()]
    if not reminders:
        print("There are no reminders")  # Print message to console
        speak("There are no reminders")



def send_email(receiver_add, subject, message):
    msg = MIMEMultipart()
    msg['From'] = 'naturephotography182@gmail.com'
    msg['To'] = receiver_add
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('naturephotography182@gmail.com', 'pxbd njks qeij bmig')
        text = msg.as_string()
        server.sendmail('naturephotography182@gmail.com', receiver_add, text)
        server.quit()
        return True
    except Exception as e:
        print(str(e))
        return False