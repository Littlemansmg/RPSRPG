

import time
import os
import Roshambo as REG
import Battle_objects

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
            player1health = deterHealth(player1option)
            player2health = deterHealth(player2option)
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
                    tmpattack = Battle_objects.attacks()
                    oneattack = tmpattack.tackle()
                    twoattack = tmpattack.struggle()
                    print(player1health, player2health)
                    print(first + " did " + oneattack + " damage.\n")
                    time.sleep(3)
                    oneattack = int(oneattack)
                    player2health = player2health - oneattack

                    end = winner(player1health, player2health)

                    if end == 0:
                        break

                    print(second + " did " + twoattack + " damage.\n")
                    time.sleep(3)
                    twoattack = int(twoattack)
                    player1health = player1health - twoattack

                    end = winner(player1health, player2health)

                    if end == 0:
                        break

                if first == player2option and second == player1option:
                    tmpattack = Battle_objects.attacks()
                    oneattack = tmpattack.tackle()
                    twoattack = tmpattack.struggle()
                    print(player1health, player2health)
                    print(first + " did " + oneattack + " damage.\n")
                    time.sleep(3)
                    oneattack = int(oneattack)
                    player1health = player1health - oneattack

                    end = winner(player1health, player2health)

                    if end == 0:
                        break

                    print(second + " did " + twoattack + " damage.\n")
                    time.sleep(3)
                    twoattack = int(twoattack)
                    player2health = player2health - twoattack

                    end = winner(player1health, player2health)

                    if end == 0:
                        break

def deterHealth(option):
    if option == "Rock":
        return Battle_objects.rock.health
    elif option == "Paper":
        return Battle_objects.paper.health
    elif option == "Scissors":
        return Battle_objects.scissors.health

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
