# # string concatenation (put strings together)
# text = "Daffa" # string variable

# # a few ways to do this
# print("Hello " + text)
# print("Hello {}".format(text))
# print(f"Hello {text}")

import code, hp, hungergames, zombie
import random

print("Welcome to Mad Libs! This is a word game where you input a word to substitute for blanks in a story. The goal is to create the wackiest story when read aloud.")

# this if statement is like main() in Java
# it only runs when the file is executed as a script, but not as a module
if __name__ == "__main__":
    m = random.choice([code, hp, hungergames, zombie])
    m.madlib()