"""
Hangman The Game
Created by Chetsadaporn Traivinidsreesuk
"""


import random
import os


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
            break
        elif response == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            endgame()
            break
        elif response == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            tutorial()
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
    return random.choice(wordbank)


def thegame():
    "This function is where the game take place."


def tutorial():
    """Print information of how to play the game"""
    print("Guess the word! Choose a cagetory you interested in and ")
    print()
    print("Press ENTER to continue.")
    input("")
    os.system('cls' if os.name == 'nt' else 'clear')

def endgame():
    """Exit the game and export log file"""


mainmenu(0)
