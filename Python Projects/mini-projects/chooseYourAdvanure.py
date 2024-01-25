# here i tried to make a clip of a visual novel
def monsterFight():
    print("After recieving blessing from the angle you open the door and see the monster again")
    print("now have the power to fight the monster")
    print("you fight the moster and won the battle")
    print("you are now free from the dark room")
# ----------documentation for opening window part----------------
def window():
    answerForWindow = input("open the window? y/n: ")
    if(answerForWindow == "y"):
        print("You open the window and see a beautiful garden.")
        print("You jump out of the window and meet an angle")
        print("the angle asked you what do you want?")
        answerForAngle = input("rich/poor/hero/strong/theif/love: ")
        if(answerForAngle == "rich"):
            print("You become rich but there is no way to spend the money.")
        elif(answerForAngle == "poor"):
            print("who cares you were poor from the beginning.")
        elif(answerForAngle == "hero" or answerForAngle == "strong"):
            print("The angle smiles and give you a sword and sheild ")
            monsterFight()
        elif(answerForAngle == "theif"):
            print(" NO ONE LIKE THEIF GAME OVER BITCH")
            exit()
        elif(answerForAngle=="love"):
            print("The angle gives you a kiss and you obtain the strenght of 1M MAN")
            monsterFight()
            confession = input("angle proposed you: DO YOU WANT TO MARRY? ME? ")
            if(confession == "yes"):
                print("YOU are married and live happily")
            elif(confession =='no'):
                print("JERK END")
            
        else:
            print("you die in confusion")
    else:
            print("You stay in the room forever and die of loneliness.")
#----------------------------------------------------------------

name = input("Enter Name to continue: ")
print(f" WELCOME {name} TO THE NEW WORLD!")
print("You are in a dark room.")
print("You can see a door and a window.")
print("Which one do you choose?")
answerForDoorWindow = input("door/window: ")
if(answerForDoorWindow == "door"):
    print("You open the door and see a monster.")
    print("What do you do?")
    answerForMonster = input("fight/run: ")
    if(answerForMonster == "fight"):
        print("You fight the monster and die.")
    elif(answerForMonster == "run"):
        print("You run away and lock the door.")
        print("You are safe now.")
        print("You are in a dark room again the only option is window do you want to open the window?.")
        window()
else:
    window()     
