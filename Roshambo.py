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
    DONE A. Health and Damage
    B. Bonuses against each other ex. rock weaker than paper
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
import RPG
# vars
choices = ["Rock", "Paper", "Scissors"]

# REGULAR GAME FUNCTIONS

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

# BATTLE GAME FUNCTIONS

# PLAY BATTLE GAME
def battleGame():

    while True:
        os.system('cls')
        try:
            option = input("How would you like to play?\n"
                           "  1: ai vs ai\n"
                           "  2: player vs ai\n"
                           "  3: player vs player\n"
                           "  4: quit\n")
            option = int(option)

            if option == 1:
                player1option = choices[aiChoice()]
                player2option = choices[aiChoice()]
            elif option == 2:
                player1option = choices[playerChoice()]
                player2option = choices[aiChoice()]
            elif option == 3:
                player1option = choices[playerChoice()]
                player2option = choices[playerChoice()]
            elif option == 4:
                break
            else:
                print("Learn how to read, Idiot.")
                time.sleep(3)
                continue

        except (ValueError, TypeError):
            print("That ain't gonna work here.\n")
            time.sleep(3)
            os.system('cls')
        if player1option != "":
            # BATTLE GAME

            # player1health = 20
            player2health = 20
            try:
                order = input("Who gets to go first, Player 1 or Player 2? (Type 1 / 2)\n")
                order = int(order)
                if order == 1:
                    first = player1option
                    second = player2option
                else:
                    first = player2option
                    second = player1option
            except:
                print("Learn to read.")
                time.sleep(2)
                break

            while True:
                os.system('cls')

                if first == player1option and second == player2option:
                    oneattack = tackle()
                    twoattack = tackle()
                    print(RPG.rock.health, player2health)
                    print(first + " did " + oneattack + " damage.\n")
                    time.sleep(3)
                    oneattack = int(oneattack)
                    player2health = player2health - oneattack

                    end = winner(RPG.rock.health, player2health)

                    if end == 0:
                        break

                    print(second + " did " + twoattack + " damage.\n")
                    time.sleep(3)
                    twoattack = int(twoattack)
                    RPG.rock.health = RPG.rock.health - twoattack

                    end = winner(RPG.rock.health, player2health)

                    if end == 0:
                        break

                if first == player2option and second == player1option:
                    oneattack = tackle()
                    twoattack = tackle()
                    print(RPG.rock.health, player2health)
                    print(first + " did " + oneattack + " damage.\n")
                    time.sleep(3)
                    oneattack = int(oneattack)
                    RPG.rock.health = RPG.rock.health - oneattack

                    end = winner(RPG.rock.health, player2health)

                    if end == 0:
                        break

                    print(second + " did " + twoattack + " damage.\n")
                    time.sleep(3)
                    twoattack = int(twoattack)
                    player2health = player2health - twoattack

                    end = winner(RPG.rock.health, player2health)

                    if end == 0:
                        break


def winner (p1Health, p2Health):
    close = 1
    if p1Health > 0 and p2Health <= 0:
        print("Player 1 wins!\n")
        time.sleep(3)
        close = 0
    elif p2Health > 0 and p1Health <= 0:
        print("Player 2 wins!\n")
        time.sleep(3)
        close = 0
    return close

def tackle():
    attack = rand.randrange(5, 10)
    attack = str(attack)
    return attack

# PROGRAM RUN

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
        regularGame()

    elif gameType == 2:
        battleGame()

    elif gameType == 3:
        os.system('cls')
        break

    else:
        print("Learn to read.")
        time.sleep(3)
