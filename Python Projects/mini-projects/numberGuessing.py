print("---------WELCOME TO NUMBER GUESSING GAME---------")
print("By obaidul haque")
import random
import pyttsx3
guesses = 0
container = ""
randomNumber = random.randint(0,99)
while True:
    Number = int(input("Guess the number between 0 to 99: "))
    guesses += 1
    if Number == randomNumber:
        print("You have guessed the correct number")
        
        
        break
    elif Number < randomNumber:
        print("You have guessed the smaller number")
    elif Number > randomNumber:
        print("You have guessed the bigger number")
if guesses <=5: 
    container = "You are a pro because you took "+str(guesses)+" guesses!!!"
elif 6< guesses< 10:
    container = "You are an average because you took "+str(guesses)+" guesses!!!"
else:
    contianer = "You are just dumb because you took "+str(guesses)+"guesses!!!"

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.say(container)
print(container)
engine.runAndWait()

