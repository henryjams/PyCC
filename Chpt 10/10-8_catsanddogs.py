# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 18:55:37 2022

@author: Hank
"""

file_list = ['cats.txt', 'dogs.txt']

for file in file_list:
    try:
        with open(file) as f:
            contents = f.read()
            print(contents + "\n")
    except FileNotFoundError:
        print("File not found.\n")