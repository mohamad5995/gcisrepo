import colorama as c
def aloha():
    print("helloo")

# Asks user for their name
def hello():
    name = input("Enter your name: ")
    print("hello", name)

def displayDetails():
    """This function asks the user to enter their bday information and displays it in a colored output.
    it is very fancy."""
    name = input("Enter your birth day: ")
    age = input("Enter your birth month: ")
    hobby = input("Enter your birth year: ")
    print(c.Fore.BLUE, name, c.Fore.YELLOW, age, c.Fore.RED, hobby, c.Fore.RESET)

def arithmetic(x, y):
    print("Exponent", x**y)
    print("Multiplication", x*y)
    print("Division", x/y)
    print("Floor Division", x//y)
    print("Modulus", x%y)
    print("Addition", x+y)
    print("Subtraction", x-y)

def box():
    print("*****")
    print("*   *")
    print("*****")

def birthdate():
    print("February 2nd, 2008")
# arithmetic(4,2)
# aloha()
# hello()
# displayDetails()
box()
box()
box()