# simple calculator with python
# define functions: +, -, *, /
#  print options to the user
# ask for values
# call the fxns
# while loop to continue the program until the user wants to exit

def add(a,b):
    answer = a + b
    print("The sum of " + str(a) + " and " + str(b) + " is " + str(answer) + ".")
    
def sub(a, b):
    answer = a - b
    print("The difference of " + str(a) + " and " + str(b) + " is " + str(answer) + ".")
    
def prod(a, b):
    answer = a * b
    print("The product of " + str(a) + " and " + str(b) + " is " + str(answer) + ".")
    
def div(a, b):
    answer = a / b
    print("The quotient of " + str(a) + " and " + str(b) + " is " + str(answer) + ".")

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Input your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        prod(a, b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        div(a, b)
    elif choice =="e" or choice == "E":
        print("Exit")
        quit()
        