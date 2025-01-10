#Johnny Liu
#Rock Paper Scissors
#Initialization
import random
userwins = 0
comp = 0
#Functions
def rps():
    print("Welcome to Rock, Paper, Scissors")
    while True:
        user = input("Please enter either rock, paper, or scissors, or 'end' to end the game: ")
        rps = random.randint(1,3)
        global userwins
        global comp
        score= "Your wins: " + str(userwins) + ". Computer wins: " + str(comp) + "."
        if user == "rock" and rps ==1:
            print("Computer chose rock. Tie.")
            print(score)
        elif user == "rock" and rps == 2:
            print("Computer chose paper. You lose.")
            comp = comp + 1
            print(score)
        elif user == "rock" and rps == 3:
            print("Computer chose scissors. You win.")
            userwins = userwins + 1
            print(score)
        if user == "paper"and rps ==1:
            print("Computer chose rock. You win.")
            userwins = userwins + 1
            print(score)
        elif user == "paper" and rps == 2:
            print("Computer chose paper. Tie.")
            print(score)
        elif user == "paper" and rps == 3:
            print("Computer chose scissors. You lose.")
            comp = comp + 1
            print(score)
        if user == "scissors" and rps ==1:
            print("Computer chose rock. You lose.")
            comp = comp + 1
            print(score)
        elif user == "scissors" and rps ==2:
            print("Computer chose paper. You win.")
            userwins = userwins + 1
            print(score)
        elif user == "scissors" and rps ==3:
            print("Computer chose scissors. Tie.")
            print(score)
        if user =="end":
            print("You have ended the game.")
            break
#Main
rps()
