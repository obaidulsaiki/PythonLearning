# modules  - libraries that containts functions predifined by someone else
# random - module that contains functions for generating random numbers
# to use those modules we need to import them by using import keyword

# import random
# coin toss
import sys
import statistics


def coinToss():
    import random
    coin = random.choice(["heads", "tails"])
    # here choice function returns a list of heads and tails and random function picks one of them
    print(coin)
# the alternative way to do this is using from in case of that


def optimize_coinToss():
    from random import choice
    coin = choice(["heads", "tails"])
    print(coin)


# random number between a , b
def RanNum():
    import random
    a = 1
    b = 10
    randomNumber = random.randint(a, b)
    print(randomNumber)
# shuffle randomly


def shuffles():
    import random
    cards = ["Jack", "Queen", "King", "Ace"]
    random.shuffle(cards)
    # print(cards) - this will output the python syntex shuffled list
    for card in cards:
        print(card, end=" ")  # this will output the list in a more readable way


# statistics module
def state():
    import statistics
    nums = [1, 5, 33, 12, 46, 33, 2]
    # it will output average of the list
    print(round(statistics.mean(nums), 2))


# sys module
# exit() which will exit the program
# argv() which will take the command line argument
# from the user's input
# command line argument - the argument that we pass when we run the program
# argv - argument vector
def sys_Learnin():
    import sys
    print("my name is ", sys.argv[1])
# sys.argv[0] - will print the location and name of the file
# if user dont enter anything in will give index error
# to avoid this we can use if statement or try


def optimized_Sys():
    import sys
    try:
        print("my name is ", sys.argv[1])
    except IndexError:
        print("to few argument")


def exitfunction():
    import sys
    # sys.exit() - will exit the program
    if (len(sys.argv)) != 2:
        sys.exit("to few argument")
    print("my name is ", sys.argv[1])
