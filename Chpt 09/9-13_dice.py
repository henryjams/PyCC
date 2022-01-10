# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 18:05:00 2022

@author: Hank
"""

from random import randint

class Die:
    """ this class will create a die that rolls between 1 and 6 """
    
    def __init__(self, sides):
        """ determines the number of sides """
        self.sides = sides
    
    def roll_die(self):
        """ rolls the dice with the chosen number of sides """
        print(randint(1, self.sides))
        
# six sided die
die6 = Die(6)
die6.roll_die()

# ten sided die
die10 = Die(10)
die10.roll_die()

# twenty sided die
die20 = Die(20)
die20.roll_die()