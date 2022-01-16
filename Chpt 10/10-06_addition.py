# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 18:41:58 2022

@author: Hank
"""

print("Please enter two numbers you wish to add together.")

num_one = input("First number: \n")
num_two = input("Second number: \n")

try:
    total = int(num_one) + int(num_two)
except ValueError:
    print("\nPlease only input numbers.")
else:
    print(f"\nYour total is {total}.")