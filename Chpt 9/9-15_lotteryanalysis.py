# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 19:32:19 2022

@author: Hank
"""

from random import choice

# bank of letters and numbers to pick from when creating winning combo
lottery_bank = ['A','E','R','W', 1, 2, 3, 4, 5, 6, 7, 8, 9]

tickets_bought = 0

def create_combo():
    """ this function picks four symbols at random from lottery_bank """
    combo = [] # create an empty list to generate winning combo
    i = 0
    while i < 4:
        combo.append(choice(lottery_bank))
        i += 1
    return combo

winning_ticket = create_combo()

match = False

while not match:
    """ this loop buys a ticket, increments the ticket counter, and then
        buys another if the tickets don't match """
    bought_ticket = create_combo()
    match = winning_ticket == bought_ticket
    tickets_bought += 1
    
if match:
    print("We have a winner!")
    print(f"The winning ticket was {winning_ticket}.")
    print(f"This time you bought {tickets_bought} tickets.")