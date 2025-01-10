#Johnny Liu
#1/8/24
#Multiplication Quiz

#initialization
import random

#Functions
print("Welcome to multiplication quiz")
level = input("Please select difficulty (Easy, Medium, Hard): ")
qnum = int(input("Please enter how many questions you would like to do : "))
score = 0
if level == str("Easy"):
    for i in range (qnum):
        y = random.randint(0,10)
        d = random.randint(0,10)
        print("What is " + str(y) + " x " + str(d) + "?: ")
        x = int(input("Your answer: "))
        print("Your answer: " +  str(x))
        if x == y*d:
            print("Correct!")
            score = score + 1
        else:
            print("Incorrect!")
    print("Final score: " + str(score) + " out of " + str(qnum) + " correct.")
elif level == str("Medium"):
    for i in range (qnum):
        y = random.randint(7,15)
        d = random.randint(7, 15)
        print("What is " + str(y) + " x " + str(d) + "?: ")
        x = int(input("What is " + str(y) + " x " + str(d) + "?: "))
        print("Your answer: " +  str(x))
        if x == y*d:
            print("Correct!")
        else:
            print("Incorrect!")
    print("Final score: " + str(score) + " out of " + str(qnum) + " correct.")
elif level == str("Hard"):
    for i in range (qnum):
        y = random.randint(12, 16)
        d = random.randint(12, 16)
        print("What is " + str(y) + " x " + str(d) + "?: ")
        x = int(input("What is " + str(y) + " x " + str(d) + "?: "))
        print("Your answer: " +  str(x))
        if x == y*d:
            print("Correct!")
        else:
            print("Incorrect!")
    print("Final score: " + str(score) + " out of " + str(qnum) + " correct.")

