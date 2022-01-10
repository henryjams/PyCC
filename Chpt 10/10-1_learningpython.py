# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 20:30:06 2022

@author: Hank
"""

file_name = "C:/Users/Hank/python_learning/PyCC/Chpt 10/what_i've_learned.txt"

# Reading entire file
print("\n ~ Printing by reading entire file: \n")
with open(file_name) as file:
    contents = file.read()
    
print(contents)

# For loop
print("\n\n ~ Printing with a for loop: ")
with open(file_name) as file:
    for line in file:
        print(line)

# Working outside the with block
print("\n\n ~ Creating a list and printing outside with block: \n")
with open(file_name) as file:
    lines = file.readlines()
    
for line in lines:
    print(line)