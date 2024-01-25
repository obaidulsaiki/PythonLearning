import random
print("-------WELCOME TO THE QUIZ GAME presented by: Obaidulsaiki------ ")
print("(You will be start with 0 score if you get 5 points you win)")
Questions = [
    {"What is the capital of Bangladesh? ":"Dhaka"},
    {"What is the capital of India? ":"Delhi"},
    {"What is the capital of Pakistan? ":"Islamabad"},
    {"What is the capital of China? ":"Beijing"},
    {"What is the capital of USA? ":"Washington DC"},
    {"What is the capital of UK? ":"London"},
    {"What is the capital of Japan? ":"Tokyo"},
    {"What is the capital of Russia? ":"Moscow"},
    {"What is the capital of France? ":"Paris"},
    {"What is the capital of Germany? ":"Berlin"},
]
score = 0
penalty = 0

while True:
    question = random.choice(Questions)
    for key in question:
        answer = input(key)
        if answer.lower() == question[key].lower():
            score += 1
            print("Correct! New Score: ",score)
        else:
            print("wrong!penalty 1 point")
            penalty += 1
    del Questions[Questions.index(question)]
    if(score == 5):
        print("You win the game!")
        break
    elif(penalty == 3):
        print("You lose the game!")
        break
print("final score: ",score,"points")


