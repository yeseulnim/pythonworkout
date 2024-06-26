# write a function 'guessing_game' that takes no arguments
# when run, the function chooses a random number between 0 and 100 (inclusive)
# ask the user to guess the chosen number
# each time user enters a guess, the program indicates one of the following:
# too high / too low / just right
# if the user guesses correctly, the program exits. otherwise the user is asked to try again
# only exit if user guessses correctly

from random import randint
def guessing_game():
    num = randint(0, 100)

    while guess := int(input("input the guess: ")):
        if guess > num:
            print("too high")
        elif guess < num:
            print("too low")
        else:
            print("just right")
            break

# guessing_game()



# modify the program such that it gives the user only three chances to guess the correct number
# if they try three times without success the program tells them that they didn't guess in time and exits

def guessing_game_three_tries():
    num = randint(0, 100)
    guess_count = 0
    while guess := int(input("input the guess: ")):
        if guess > num:
            print("too high")
            guess_count += 1
        elif guess < num:
            print("too low")
            guess_count += 1
        else:
            print("just right")
            break
        if guess_count == 3:
            print("out of guesses!")
            break

#guessing_game_three_tries()



# the user should choose a random number base from 2 to 16 in which they submit their input
# if the user inputs 10 as their guess, you need to interpret it in the correct number base

def guessing_game_base():
    num = randint(0, 100)
    base = int(input("input the base (2 to 16) "))

    while guess := int(input(f"input the guess in base {base}: ")):
        guess_str = str(guess)
        guess = 0
        for ind, val in enumerate(guess_str):
            guess += base ** (len(guess_str)-ind-1) * int(val)

        print(f"your guess in base 10 is {guess}")

        if guess > num:
            print("too high")
        elif guess < num:
            print("too low")
        else:
            print("just right")
            break

# guessing_game_base()



# try the same thing, but have people choose words from a dictionary
# limit to words containing two to five letters
# instead of telling the user they should guess a smaller or larger number,
# have them choose an earlier or later word in the dictionary

from urllib.request import urlopen
from random import choice

def guessing_game_word():

    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = urlopen(word_site)
    txt = response.read()
    words = txt.splitlines()
    words = [i for i in words if len(i)>1 and len(i)<6]
    word = str(choice(words), 'utf-8')

    while guess := input("input the guess: "):
        if guess > word:
            print("too late in the dictionary")
        elif guess < word:
            print("too early in the dictionary")
        else:
            print("just right")
            break

#guessing_game_word()