def getNumFromUser(prompt):
    '''Function used to get a number from the user using the prompt'''
    return int(input(prompt))

def checkEven(num):
    '''Function checks if a number is even and returns True otherwise False'''
    if num%2 == 0: # Checks if a value is divisible by 2, if it is then its even otherwise it is odd
        return True
    else:
        return False

def calculateSquare(base):
    '''Function returns the base to the power of 2'''
    return base**2

def calculateCube(base):
    '''Function returns the base to the power of 3'''
    return base**3


def main():
    x = getNumFromUser("Enter a number: ")
    if checkEven(x): # checks if number submitted by user is even or odd
        print("Even number")
    else:
        print("Odd number")
    
    square = calculateSquare(x) # Stores result of square in a variable
    print("Square:", square)
    cube = calculateCube(x) # Stores result of cube in a variable
    print("Cube:", cube)
main()