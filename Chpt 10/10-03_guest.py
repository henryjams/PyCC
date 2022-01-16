# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 19:07:14 2022

@author: Hank
"""

guest_name = input("What is your name?\n")
print("Thanks chump, your name is mine forever now.")

filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(guest_name)