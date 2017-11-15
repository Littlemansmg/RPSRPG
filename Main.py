"""
RPSRPG program created by Scott Goes 11/2/2017
Main.py created 11/14/17

 What is it?
  A game that starts as a regular game of Roshambo.
  but then turns into a RPG turn based fighter.

This main form is just calling other files to run the program.
"""

import time
import os
import Roshambo
import Battle

while True:
    # Decide between regular game and RPG battle
    os.system('cls')

    # catch a user error if they put in a letter or a wrong value
    try:
        gameType = input("What type of game would you like to play?\n"
                         "  1: Regular Rock paper Scissors\n"
                         "  2: Totally awesome RPG battle\n"
                         "  3: Quit\n")
        gameType = int(gameType)

    except (ValueError, TypeError):
        print("That ain't gonna work here.\n")
        time.sleep(3)

    # Run Game 1, 2 or quit
    if gameType == 1:
        Roshambo.regularGame()

    elif gameType == 2:
        Battle.battleMenu()

    elif gameType == 3:
        os.system('cls')
        break

    else:
        print("Learn to read.")
        time.sleep(3)
