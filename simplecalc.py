#Johnny Liu
#Simple Calculator

#Init
#Functions
def add(num1, num2):
    result = num1 + num2
    print("The result is: " +str(result))
def sub(num1, num2):
    result = num1 - num2
    print("The result is: " +str(result))
def mult(num1, num2):
    result = num1 * num2
    print("The result is: " +str(result))
def div(num1, num2):
    result = num1 / num2
    print("The result is: " +str(result))
def simplecalculator():
    print("Welcome to Simple Calculator")
while True:
    print("Select an operation: ")
    print("""1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Quit""")
    option = int(input("(1-5) Select option: "))
    if option == 1:
        int1 = int(input("Enter first number: "))
        int2 = int(input("Enter second number: "))
        add(int1, int2)
    if option == 2:
        int1 = int(input("Enter first number: "))
        int2 = int(input("Enter second number: "))
        sub(int1, int2)
    if option == 3:
        int1 = int(input("Enter first number: "))
        int2 = int(input("Enter second number: "))
        mult(int1, int2)
    if option == 4:
        int1 = int(input("Enter first number: "))
        int2 = int(input("Enter second number: "))
        div(int1, int2)
    if option == 5:
        break


#Main
simplecalculator()






