'''
Class example

class helloWorld:

    def f(self):
        return 'I\'m from the other .py file'
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
