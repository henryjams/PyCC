# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 19:26:49 2022

@author: Hank
"""

# create a new file in write mode
file_name = 'guest_book.txt'

with open(file_name, 'w') as f:
    while True:
        guest_name = input("Please enter your name for the guest book: \n")
        f.write(guest_name + "\n")
    