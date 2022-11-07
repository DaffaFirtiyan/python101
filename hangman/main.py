import urllib.request, json, string
from random import choice

with urllib.request.urlopen("https://www.randomlists.com/data/words.json") as url:
    data = json.loads(url.read().decode()) 
    data = data["data"] # convert type from "dict" to "list"

def hangman():
    word = getValidWord(data)
    known = [] # list of correctly guessed letters
    alphabet = list(string.ascii_lowercase)
    life = 7

    print(*word, sep="")

    for i in range(len(word)):
        known.append("_")
    print(*known, sep=" ")

    while "_" in known and life > 0: 
        print()
        print(f"You have {life} guesses left")
        guess = input("letter: ")

        if guess not in alphabet:
            print(f"You already guessed {guess}")
            print(*known, sep=" ")
            continue
        
        alphabet.remove(guess)
        if guess not in word:
            life -= 1
            print(f"{guess} is not in the letter")
            print(*known, sep=" ")
            continue

        for i in range(0, len(word), 1):
            if guess == word[i]:
                known.insert(i, guess)
                del known[i+1]
        print(*known, sep=" ")
    

    if "_" not in known and life > 0:
        print("You won! The word was", end=" ")
        print(*word, sep="")
    else:
        print("You lost! The word was", end=" ")
        print(*word, sep="")

# some of the words in this list contains "-" and " ", so we're going to not let the computer pick words containing those characters as a guessable word
def getValidWord(data):
    word = choice(data)
    
    while "-" in word or " " in word:
        word = choice(data)

    return list(word.lower())

hangman()