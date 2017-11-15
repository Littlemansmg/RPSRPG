'''
Battle_objects.py (previously RPG.py) created by Scottie Goes on 11/14/17

This file is for running multiple aspects of the battle game, and clears up some code.
'''
import random as rand

class rock:
    name = "Rock"
    health = 25
    defence = 3

class paper:
    name = "Paper"
    health = 23
    defence = 1

class scissors:
    name = "Scissors"
    health = 24
    defence = 2

class attacks:
    def tackle(self):
        self = rand.randrange(5, 10)
        self = str(self)
        return self

    def struggle(self):
        self = rand.randrange(1, 4)
        self = str(self)
        return self

    def defend(self):
        print("Shrug")

    def death(self):
        self = 100
        self = str(self)
        return self
