# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 18:04:54 2021

@author: Hank
"""

guests = int(input("How many in your party, please?\n"))

if guests > 8:
    print("Please go away now, that's too many people.")
else:
    print("Sure, I will make up a table right now for " + str(guests) + ".")