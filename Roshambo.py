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
import time
import os

# vars
choices = ["Rock", "Paper", "Scissors"]

def gameOption(option):
    if option == 1:
        finisher(aiChoice(), aiChoice())
    elif option == 2:
        finisher(playerChoice(), aiChoice()),
    elif option == 3:
        finisher(playerChoice(),playerChoice())

def aiChoice():
    a1 = rand.randint(0, 2)
    print(choices[a1])
    return a1

def playerChoice():
    pPick = input("Rock: 1\n"
                "Paper: 2\n"
                "Scissors: 3\n")
    pPick = int(pPick) -1
    return pPick

def finisher(player1, player2):
    # Rock wins
    if player1 == 0 and player2 == 2:
        print("AI 1 wins!")

    # Rock loses
    elif player1 == 0 and player2 == 1:
        print("AI 1 loses!")

    # Paper Wins
    elif player1 == 1 and player2 == 0:
        print("AI 1 wins!")

    # Paper Loses
    elif player1 == 1 and player2 == 2:
        print("AI 1 loses!")

    # Scissors wins
    elif player1 == 2 and player2 == 1:
        print("AI 1 wins!")

    # Scissors loses
    elif player1 == 2 and player2 == 0:
        print("AI 1 loses!")

    # if a tie happens
    else:
        print("The AI's tied!")


#PROGRAM RUN



#while True:
#    os.system('cls')

#  REGULAR GAME
#  Commented out for Fight testing.
#    try:
#        option = input("Would you like to do?\n"
#                    "  1: ai vs ai\n"
#                    "  2: player vs ai\n"
#                    "  3: player vs player\n"
#                    "  4: quit\n")
#        option = int(option)
#
#        if option < 4 and option > 0:
#            gameOption(option)
#        elif option == 4:
#            break
#        else:
#            print("Learn how to read, Idiot.")
#    except (ValueError, TypeError):
#        print("That ain't gonna work here.\n")
#    time.sleep(3)
#    os.system('cls')




