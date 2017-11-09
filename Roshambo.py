'''
RPSRPG created by Scott Goes 11/2/2017

 What is it?
  A game that starts as a regular game of Roshambo.
  but then turns into a RPG turn based fighter.

 TODO
  DONE 1. AI generated Roshambo game
  DONE 2. 1 player option
  DONE 3. 2 player option
  FUCKED 4. OPTIONAL GUI
  5. RPG Aspects
    A. Health and Damage
    B. Bonuses against each other ex. rock stronger than paper
    C. Critical hits

Runs functions/classes from another python file.
  from RPG import helloWorld
  hello = helloWorld()
  print (hello.f())
'''


# imports
import random as rand
import time
import os

# vars
choices = ["Rock", "Paper", "Scissors"]

# REGULAR GAME FUNCTIONS

# function is calling other functions and returns nothing.
def gameOption(option):
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
    print(choices[a1])
    return a1

# callable fucntion to get user choice
def playerChoice():
    pPick = input("What do you pick?\n"
                  "Rock: 1\n"
                  "Paper: 2\n"
                  "Scissors: 3\n")
    pPick = int(pPick) -1
    return pPick

# winning logic that requires 2 paramaters.
def finisher(player1, player2):
    # Rock wins
    if player1 == 0 and player2 == 2:
        print("Player 1 wins!")

    # Rock loses
    elif player1 == 0 and player2 == 1:
        print("Player 2 wins!")

    # Paper Wins
    elif player1 == 1 and player2 == 0:
        print("Player 1 wins!")

    # Paper Loses
    elif player1 == 1 and player2 == 2:
        print("Player 2 wins!")

    # Scissors wins
    elif player1 == 2 and player2 == 1:
        print("Player 1 wins!")

    # Scissors loses
    elif player1 == 2 and player2 == 0:
        print("Player 2 wins!")

    # if a tie happens
    else:
        print("The Players tied!")

# BATTLE GAME FUNCTIONS

def tackle():
    attack = rand.randrange(5, 10)

# PROGRAM RUN

# Decide between regular game and RPG battle
while True:
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

        # REGULAR GAME
        while True:
            os.system('cls')

            # catch a user error if they put in a letter or a wrong value
            try:
                option = input("How would you like to play?\n"
                               "  1: ai vs ai\n"
                               "  2: player vs ai\n"
                               "  3: player vs player\n"
                               "  4: quit\n")
                option = int(option)

                # passes option to the gameOption function or quits.
                if option < 4 and option > 0:
                    gameOption(option)
                elif option == 4:
                    break
                else:
                    print("Learn how to read, Idiot.")
            except (ValueError, TypeError):
                print("That ain't gonna work here.\n")
                time.sleep(3)
                os.system('cls')

    elif gameType == 2:
        os.system('cls')
        # Battle game
        player1health = 20
        player2health = 20
        print("Player 1 gets to go first.")
        time.sleep(2)
        while True:
            os.system('cls')
            oneattack = tackle()
            oneattack = str(oneattack)
            twoattack = tackle()
            twoattack = str(twoattack)
            print(player1health,player2health)
            print("Rock did " + oneattack + " damage.\n")
            time.sleep(3)
            oneattack = int(oneattack)
            player2health = player2health - oneattack
            if player1health > 0 and player2health <= 0:
                print("Player 1 wins!\n")
                time.sleep(3)
                break
            print("Paper did " + twoattack + " damage.\n")
            time.sleep(3)
            twoattack = int(twoattack)
            player1health = player1health - twoattack
            if player2health > 0 and player1health <= 0:
                print("Player 2 wins!")
                time.sleep(3)
                break




    elif gameType == 3:
        os.system('cls')
        break

    else:
        print("Learn to read.")
        time.sleep(3)
