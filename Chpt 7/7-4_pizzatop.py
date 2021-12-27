# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 20:37:46 2021

@author: Hank
"""

intro = "\nCiao, let's-a make-a pizza!"
prompt = "Which topping would you like to add?"

print(intro)

active = True
while active:
    topping = input(prompt)
    if topping != "quit":
        print("Okay, I'll go ahead and add " + str(topping) + ".")
    
    if topping == "quit":
        active = False
        print("Okay, see you next-a time.")
    