'''
class helloWorld:

    def f(self):
        return 'I\'m from the other .py file'
'''

#imports
import random as rand

class rock:
    health = 12

    def tackle(self):
        attack = rand.randrange(3, 8)

class paper:
    health = 8

    def tackle(self):
        attack = rand.randrange(4, 8)

class scissors:
    health = 10

    def tackle(self):
        attack = rand.randrange(4, 7)

