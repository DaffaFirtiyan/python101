from random import randrange

def computerGuess(c):
    i = 1
    guess = randrange(11)

    while guess != c:
        print(f"The computer picked {guess}")
        i += 1
        guess = randrange(11)

    print(f"The computer took {i} guesses")

# computerGuess(int(input("Pick a number between 0 - 10: ")))
computerGuess(1)