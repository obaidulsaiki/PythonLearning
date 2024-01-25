import random
print("----------------Welcome to Rock, Paper, Scissors!---------------------")
print("You will be playing against the computer.")
print("The first to 3 wins is the winner!")
print("Game by obaidulsaiki")
container = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0
while True:
    if player_score >2 or computer_score >2:
        print("Game over!")
        break
    playerInput = input("rock/paper/scissos: ")
    computerChoice = random.choice(container)
    if playerInput == "rock" and computerChoice =="scissiors":
        print("You win!")
        player_score += 1
    elif playerInput == "paper" and computerChoice =="rock":
        print("You win!")
        player_score += 1
    elif playerInput == "scissors" and computerChoice =="paper":
        print("You win!")
        player_score += 1
    elif playerInput == computerChoice:
        print("It's a tie!")
    else:
        print("You lose!")
        computer_score += 1
print(f"Your score: {player_score}")
print(f"Computer score: {computer_score}")
