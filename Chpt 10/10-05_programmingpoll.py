# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 19:26:49 2022

@author: Hank
"""

# create a new file in write mode
file_name = 'programming_poll.txt'

with open(file_name, 'w') as f:
    while True:
        guest_name = input("Why do you like programming? \n")
        f.write(guest_name + "\n")
        print("Thank you for your response.")
    