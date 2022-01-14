# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 22:16:27 2022

@author: Hank
"""

file_name = "C:/Users/Hank/python_learning/PyCC/Chpt 10/what_i've_learned.txt"

# Replacing every instance of 'Python' with 'C'
print("\n\n ~ Creating a list and printing outside with block: \n")
with open(file_name) as file:
    lines = file.readlines()
    
for line in lines:
    print(line.replace('python','C')) 