# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:50:52 2021

@author: Hank
"""

prompt = "Would you like to rent a car?\n"
if input(prompt) == 'yes' or 'Yes' or 'y':
    car = input("What kind of car would you like to rent?\n")
    print("Let me see if I can find you a " + car.title() + ".")
else:
    print("Thank you for leaving now.")
    
