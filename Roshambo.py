"""
Roshambo.py created by Scottie Goes on 11/2/17

This is the regular rock paper scissors game.

TODO
    Finished
"""

# imports
import random as rand
import time
import os

# vars
choices = ["Rock", "Paper", "Scissors"]

# function is calling other functions and returns nothing.
def regGameOption(option):
    if option == 1:
        #ai game
        finisher(aiChoice(), aiChoice())
    elif option == 2:
        #1 player game
        finisher(playerChoice(), aiChoice()),
    elif option == 3:
        #2 player game
        finisher(playerChoice(),playerChoice())

# callable function to get ai choice
def aiChoice():
    a1 = rand.randint(0, 2)
    print("AI picked")
    print(choices[a1])
    print()
    time.sleep(2)
    return a1

# callable fucntion to get user choice
def playerChoice():
    pPick = input("What do you pick?\n"
                  "Rock: 1\n"
                  "Paper: 2\n"
                  "Scissors: 3\n")
    pPick = int(pPick) -1
    print ("You picked " + choices[pPick])
    time.sleep(2)
    return pPick

# winning logic that requires 2 paramaters.
def finisher(player1, player2):
    # Rock wins
    if player1 == 0 and player2 == 2:
        print("Player 1 wins!")
        time.sleep(3)

    # Rock loses
    elif player1 == 0 and player2 == 1:
        print("Player 2 wins!")
        time.sleep(3)

    # Paper Wins
    elif player1 == 1 and player2 == 0:
        print("Player 1 wins!")
        time.sleep(3)

    # Paper Loses
    elif player1 == 1 and player2 == 2:
        print("Player 2 wins!")
        time.sleep(3)

    # Scissors wins
    elif player1 == 2 and player2 == 1:
        print("Player 1 wins!")
        time.sleep(3)

    # Scissors loses
    elif player1 == 2 and player2 == 0:
        print("Player 2 wins!")
        time.sleep(3)
    # if a tie happens
    else:
        print("The Players tied!")
        time.sleep(3)

# PLAY REGULAR GAME
def regularGame():
    while True:
        os.system('cls')
        try:
            option = input("How would you like to play?\n"
                           "  1: ai vs ai\n"
                           "  2: player vs ai\n"
                           "  3: player vs player\n"
                           "  4: quit\n")
            option = int(option)

            if option < 4 and option > 0:
                regGameOption(option)
            elif option == 4:
                break
            else:
                print("Learn how to read, Idiot.")
        except (ValueError, TypeError):
            print("That ain't gonna work here.\n")
            time.sleep(3)
            os.system('cls')