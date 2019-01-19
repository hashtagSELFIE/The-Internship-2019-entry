"""
Hangman The Game
Created by Chetsadaporn Traivinidsreesuk
"""


import random
import os
from ast import literal_eval


def mainmenu(menucount):
    """Main menu for navigating through option and gameplay."""
    while 1:
        if menucount != 0:
            print("Welcome back to Hangman The Game!")
        else:
            print("Welcome to the Hangman The Game!")
        print()
        print("Type in 1 to PLAY")
        print("Type in 2 to LEARN HOW TO PLAY")
        print("Type in 3 to EXIT")
        print()
        response = input()
        if response == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            thegame()
        elif response == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            tutorial()
        elif response == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            endgame()
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid input, Please type again!")
            print()
        menucount += 1


def wordselector(category):
    """Return Word that will be used for that round"""
    text_selx = category + ".txt"
    realtext = open(text_selx, "r")
    wordbank = [i for i in realtext]
    return literal_eval(random.choice(wordbank))


def thegame():
    "This function is where the game take place."
    while 1:
        print("Pick your category you interested in")
        print()
        print("Type in 1 for FRUITTY FRESHNESS")
        print("Type in 2 for THRILLING TRANSPORTATION")
        print("Type in 3 for CONTINENTAL COUNTRIES")
        print()
        response = input()
        mystery = ""
        if response == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            mystery = wordselector("fruits")
            break
        elif response == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            mystery = wordselector("transportaion")
        elif response == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            mystery = wordselector("countries")
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid input, Please type again!")
            print()
    strike = len(mystery[0]) // 2
    board = ["_" for _  in mystery[0]]
    guessed = []
    os.system('cls' if os.name == 'nt' else 'clear')
    print("The game will now begin when you type in your character")
    print()
    print("Here is your mystery word.")
    for k in board:
        print(k, end=' ')
    print()
    print("Hints :", mystery[1])
    if strike > 1:
        print("You now have %i strikes left" % strike)
    else:
        print("You now have %i strike left" % strike)
    print("The game will now begin when you type in your character")
    print()
    while 1:
        answer = input()
        answer = answer.upper()
        if answer.isalpha() is False:
            print("Invalid input, Please enter another character.")
            continue
        if len(answer) > 1:
            print("You must type in ONE character only. Please enter it again")
            continue
        for j in len(mystery[0]):
            if answer in mystery[0]:
                board[j] = answer
                


    os.system('cls' if os.name == 'nt' else 'clear')


def tutorial():
    """Print information of how to play the game"""
    print("Guess the word! Choose a cagetory you interested in and the game will start!")
    print("Guess the word one letter at a time. Strike is based on the length of the mystery word.")
    print("Wrong guess will result in strike! If you have enough strikes, the game will be over!")
    print()
    print("Type wisely.")
    print()
    print("Press ENTER to continue.")
    print()
    input("")
    os.system('cls' if os.name == 'nt' else 'clear')


def endgame():
    """Exit the game and export log file"""


mainmenu(0)
