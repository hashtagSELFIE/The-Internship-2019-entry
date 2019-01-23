"""
Hangman The Game
Created by Chetsadaporn Traivinidsreesuk
"""


import random
import os
from ast import literal_eval


def mainmenu(menucount, scoreboard, losecount, wincount, finalscore):
    """Main menu for navigating through option and gameplay."""
    while 1:
        if menucount != 0:
            print("Welcome back to Hangman The Game!\n")
        else:
            print("Welcome to the Hangman The Game!\n")
        print("Enter 1 for THE GAME\nEnter 2 for TUTORIAL\nEnter 3 for RESULTS & EXIT\n")
        response = input()
        if response == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            scoreboard.append(filepicker(finalscore))
        elif response == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            tutorial()
        elif response == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            endgame(scoreboard, losecount, wincount, finalscore)
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid input, Please type again!\n")
        menucount += 1


def filepicker(finalscore):
    """Selects the file that will be used in the game"""
    while 1:
        print("Pick your category you interested in\n")
        print("Type in 1 for FRUITTY FRESHNESS")
        print(
            "Type in 2 for THRILLING TRANSPORTATION\nType in 3 for CONTINENTAL COUNTRIES\n")
        if finalscore > 2499:
            print("SECRET MODE UNLOCKED!\nType in SUDO for more.")
        response = input()
        mystery = ""
        if response == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            mystery = wordselector("fruits.txt")
            break
        elif response == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            mystery = wordselector("transportaion.txt")
            break
        elif response == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            mystery = wordselector("countries.txt")
            break
        elif response == "SUDO" and finalscore > 2499:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You have now unlocked SUDO mode! You can now enter your own custom\
 word libary. all you have to do is create an .txt file with the format below \n\n\
 ["'x'", "'y'"]\n\nOnly replace the x for the mystery text and y for hint messages\n\
 (DO NOT REMOVE DOUBLEQUOTES). And put them in the same directory as this file!\n\n\
 Please enter your custom file below\n\nType in "'!EXIT'" if you want to leave\n")
            filename = input()
            if filename == "!EXIT" or filename == "'!EXIT'":
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                mystery = wordselector(filename)
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
    realtext = open(category, "r")
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
            print("Uh oh! You have lost! The correct answer is\n\n" +
                  mystery[0] + ".\n")
            print("Press ENTER to continue.\n")
            input("")
            break
        if points == len(mystery[0]):
            results = len(mystery[0]) * 100 + strike * 50
            print(*board, sep=' ')
            print()
            print("Congratulations! You have won!\nYou have earned " + str(results)
                  + " points\nPress ENTER to continue.\n")
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
        os.system('cls' if os.name == 'nt' else 'clear')
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
                hitormiss, points = hitormiss + 1, points + 1
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
    print("You have earned %i points, good job!" % finalscore if finalscore > 1
          else "You have not won any point :(")
    print()
    print("Enter 1 to exit the program.\nEnter 2 to return to the menu.\n")
    response = input()
    if response == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif response == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        mainmenu(0, [], losecount, wincount, finalscore)


mainmenu(0, [], 0, 0, 0)
