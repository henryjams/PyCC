# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 18:17:56 2022

@author: Hank
"""

from random import choice

# bank of letters and numbers to pick from when creating winning combo
lottery_bank = ['A','E','R','W', 1, 2, 3, 4, 5, 6, 7, 8, 9]

# create an empty list to generate winning combo
winning_combo = []

def create_combo():
    """ this function picks four symbols at random from lottery_bank """
    i = 0
    while i < 4:
        winning_combo.append(choice(lottery_bank))
        i += 1
    print(winning_combo)
    
create_combo()