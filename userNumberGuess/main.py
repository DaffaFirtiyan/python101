from random import randrange

def userGuess(c):
    guess = None
    i = 0
    print("The computer picked a number between 0 - 10")

    while c != guess:
        i += 1
        guess = int(input("Number: "))
        if guess < c:
            print("Too low")
        elif guess > c:
            print("Too high")
    
    print(f"The number was {c}. \nIt took you {i} guesses!")

userGuess(randrange(10))