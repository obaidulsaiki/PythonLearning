# text to speech in python
# pip install pyttsx3
# pyttsx3 is python text to speech version 3
import cowsay
import pyttsx3
# taking a varibale to initialize pytttsx3
engine = pyttsx3.init()
# mytext = "Hello, I am a python programmer"
mytext = input("Enter your text: ")
cowsay.cow(mytext)
engine.say(mytext)
engine.runAndWait()  # this will wait untill the python program is running
