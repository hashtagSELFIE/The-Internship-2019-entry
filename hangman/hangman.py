"""
Hangman The Game
Created by Chetsadaporn Traivinidsreesuk
"""


import random
import os
from ast import literal_eval


def mainmenu(menucount):
    """Main menu for navigating through option and gameplay."""
    scoreboard = []
    while 1:
        if menucount != 0:
            print("Welcome back to Hangman The Game!\n")
        else:
            print("Welcome to the Hangman The Game!\n")
        print("Enter 1 to PLAY\nEnter 2 to LEARN HOW TO PLAY\nEnter 3 to EXIT\n")
        response = input()
        if response == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            scoreboard.append(filepicker())
        elif response == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            tutorial()
        elif response == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            endgame(scoreboard, 0, 0, 0)
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid input, Please type again!\n")
        menucount += 1


def filepicker():
    """Selects the file that will be used in the game"""
    while 1:
        print("Pick your category you interested in\n")
        print("Type in 1 for FRUITTY FRESHNESS")
        print("Type in 2 for THRILLING TRANSPORTATION\nType in 3 for CONTINENTAL COUNTRIES\n")
        response = input()
        mystery = ""
        if response == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            mystery = wordselector("fruits")
            break
        elif response == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            mystery = wordselector("transportaion")
            break
        elif response == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            mystery = wordselector("countries")
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid input, Please type again!")
            print()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("The game will now begin when you type in your character\n")
    print("Here is your mystery word.")
    outcome = thegame(mystery, 0, len(mystery[0]) // 2, [], [])
    return outcome

def wordselector(category):
    """Return Word that will be used for that round"""
    text_selx = category + ".txt"
    realtext = open(text_selx, "r")
    wordbank = [i for i in realtext]
    return literal_eval(random.choice(wordbank))


def thegame(mystery, points, strike, guessed, wrongguessed):
    "This function is where the game take place."
    board = ["_" for _ in mystery[0]]
    while 1:
        results = 0
        hitormiss = 0
        wrongguessed.sort()
        if strike == 0:
            print("Uh oh! You have lost! The correct answer is\n\n" + mystery[0] + ".\n")
            print("Press ENTER to continue.\n")
            input("")
            break
        if points == len(mystery[0]):
            results = len(mystery[0]) * 100 + strike * 50
            print(*board, sep=' ')
            print()
            print("Congratulations! You have won!\nYou have earned "+str(results)\
+" points\nPress ENTER to continue.\n")
            input("")
            break
        print(*board, sep=' ')
        print()
        print("Hints :", mystery[1])
        print("You now have %i strikes left." % strike if strike > 1 else "You \
now have 1 strike left.")
        if wrongguessed:
            print("You have incorrectly guessed:", end=' ')
            print(*wrongguessed, sep=', ')
        print()
        answer = input().upper()
        print()
        if answer.isalpha() is False:
            print("Invalid input. Please enter another character.\n")
            continue
        if len(answer) > 1:
            print("You must type in ONE character only. Please enter it again.\n")
            continue
        if answer in guessed:
            print("You have already guessed that one. Please try again.\n")
            continue
        for j in range(len(mystery[0])):
            if answer in mystery[0][j]:
                hitormiss, points = hitormiss + 1, points+1
                board[j] = answer
                continue
        if hitormiss == 0:
            print("%s is not in the mystery word!\n" % answer)
            strike -= 1
            wrongguessed.append(answer)
        elif hitormiss > 0:
            print("%s is in the mystery word!\n" % answer)
        guessed.append(answer)
    os.system('cls' if os.name == 'nt' else 'clear')
    return results

def tutorial():
    """Print information of how to play the game"""
    print("Guess the word! Choose a cagetory you interested in and the game will start!")
    print("Guess the word one letter at a time. Strike is based on the length of the mystery word.")
    print("Wrong guess will result in strike! If you have enough strikes, the game will be over!\n")
    print("Type wisely.\n")
    print("Press ENTER to continue.\n")
    input("")
    os.system('cls' if os.name == 'nt' else 'clear')


def endgame(scorelog, losecount, wincount, finalscore):
    """Exit the game and show final results"""
    for logger in scorelog:
        if int(logger) == 0:
            losecount += 1
        else:
            wincount += 1
            finalscore += int(logger)
    if wincount > 0:
        print("You have won %i times." % wincount if wincount > 1 else "You have won\
 1 time.", end=' ')
    if losecount > 0:
        print("You have lost %i times." % losecount if losecount > 1 else "You \
have lost 1 time.", end=' ')
    print("You have earned %i points, good job!" % finalscore if finalscore > 1 \
else "You have not won any point :(")
    print()
    print("Enter 1 to exit the program.\nEnter 2 to return to the menu.\n")
    response = input()
    if response == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif response == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        mainmenu(0)
mainmenu(0)
