"""
Battle.py created by Scottie Goes on 11/14/17

This file is separating the regular and the battle game to make for some cleaner code.

TODO
 DONE 1. Health and Damage
 DONE 2. Defence calculating
 3. Advantages
 4. Crits
 5. Idk. probably something to do with penis.
"""

import time
import os
import Roshambo as REG
import Battle_objects
from Battle_objects import rock as ROCK
from Battle_objects import paper as PAPER
from Battle_objects import scissors as SCISSORS

# PLAY BATTLE GAME
def battleMenu():

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
                player1option = REG.choices[REG.aiChoice()]
                player2option = REG.choices[REG.aiChoice()]
            elif option == 2:
                player1option = REG.choices[REG.playerChoice()]
                player2option = REG.choices[REG.aiChoice()]
            elif option == 3:
                player1option = REG.choices[REG.playerChoice()]
                player2option = REG.choices[REG.playerChoice()]
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
            PLAYER1 = deterObj(player1option)
            PLAYER2 = deterObj(player2option)
            try:
                order = input("Who gets to go first, Player 1 or Player 2? (Type 1 / 2)\n")
                order = int(order)
                if order == 1:
                    first = player1option
                    second = player2option
                elif order == 2:
                    first = player2option
                    second = player1option
            except(ValueError, TypeError):
                print("Learn to read.")
                time.sleep(2)
                break

            while True:
                os.system('cls')

                if first == player1option and second == player2option:
                    tmpattack = Battle_objects.attacks()
                    oneattack = tmpattack.tackle()
                    twoattack = tmpattack.tackle()
                    print(PLAYER1.health, PLAYER2.health)
                    print(PLAYER1.name + " did " + oneattack + " damage.\n")
                    time.sleep(3)
                    oneattack = int(oneattack) - PLAYER2.defence
                    PLAYER2.health -= oneattack

                    end = winner(PLAYER1.health, PLAYER2.health)

                    if end == 0:
                        break

                    print(PLAYER2.name + " did " + twoattack + " damage.\n")
                    time.sleep(3)
                    twoattack = int(twoattack) - PLAYER1.defence
                    PLAYER1.health -= twoattack

                    end = winner(PLAYER1.health, PLAYER2.health)

                    if end == 0:
                        break

                if first == player2option and second == player1option:
                    tmpattack = Battle_objects.attacks()
                    oneattack = tmpattack.tackle()
                    twoattack = tmpattack.struggle()
                    print(PLAYER1.health, PLAYER2.health)
                    print(PLAYER2.name + " did " + oneattack + " damage.\n")
                    time.sleep(3)
                    oneattack = int(oneattack)
                    PLAYER1.health = twoattack - PLAYER1.defence

                    end = winner(PLAYER1.health, PLAYER2.health)

                    if end == 0:
                        break

                    print(PLAYER2.name + " did " + twoattack + " damage.\n")
                    time.sleep(3)
                    twoattack = int(twoattack)
                    PLAYER2.health = oneattack - PLAYER2.defence

                    end = winner(PLAYER1.health, PLAYER1.health)

                    if end == 0:
                        break



def deterObj(option):
    if option == "Rock":
        return ROCK()
    elif option == "Paper":
        return PAPER()
    elif option == "Scissors":
        return SCISSORS()

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
