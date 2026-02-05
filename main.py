main.py
from kivy.app import App
from kivy.uix.label import Label
import threading
import speech_recognition as sr
import pyttsx3

from offline_ai import reply
from memory import load, save

engine = pyttsx3.init()
engine.setProperty("rate", 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def voice_loop():
    r = sr.Recognizer()
    memory = load()
    speak("A R I S online. Say Hey Aris.")

    while True:
        with sr.Microphone() as source:
            try:
                audio = r.listen(source, timeout=3, phrase_time_limit=4)
                heard = r.recognize_google(audio).lower()

                if "hey aris" in heard:
                    speak("I am listening.")
                    audio = r.listen(source, timeout=4)
                    command = r.recognize_google(audio)

                    response = reply(command, memory)
                    save(memory)
                    speak(response)
            except:
                pass

class ArisApp(App):
    def build(self):
        threading.Thread(target=voice_loop, daemon=True).start()
        return Label(text="🤖 A.R.I.S ONLINE\nSay: Hey Aris", font_size=28)

ArisApp().run()
