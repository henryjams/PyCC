# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 11:16:21 2021

@author: Hank
"""

greeting = "Welcome to AMC 'to the moon' Theater!"

print(greeting)

prompt = "What is the age of the patron?" 
prompt += "\nIf finished, type 'done'."

while True:
    age = input(prompt)
    
    if age == 'done':
        print("\tThank you for your patronage!")
        break
    
    age = int(age)
    
    if age < 4:
        print("Cost: free")
    elif age < 13:
        print("Cost: $10")
    else: 
        print("Cost: $15")
    