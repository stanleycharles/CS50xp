# Version 1

import pyttsx3

engine = pyttsx3.init()
engine.say("Hello, world")
engine.runAndWait()

# Version 2

import pyttsx3

engine = pyttsx3.init()
name = input("What's your name? ")
engine.say("Hello, {name}")
engine.runAndWait()