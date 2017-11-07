'''
class helloWorld:

    def f(self):
        return 'I\'m from the other .py file'

###BECAUSE I AM TO LAZY TO GET THIS TO WORK RIGHT NOW
###I'M GOING TO DO IT ALL IN ROSHAMBO.PY


#imports
import random as rand

class rock:
    name = 'Dwane'
    health = 12
    attack = rand.randrange(3, 8)

    def tackle(self):
        attack = rand.randrange(3, 8)
        attack = str(attack)

class paper:
    name = 'Pauper'
    health = 8

    def tackle(self):
        attack = rand.randrange(4, 8)
        return attack

class scissors:
    name = 'Syther'
    health = 10

    def tackle(self):
        attack = rand.randrange(4, 7)
        return attack
'''