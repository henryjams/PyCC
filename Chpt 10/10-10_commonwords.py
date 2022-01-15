# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 19:15:17 2022

@author: Hank
"""

book_list = ['beowulf.txt', 'the_fourth_dimension.txt', 'around_the_world.txt']

for book in book_list:
    try:
        with open(book, encoding = 'utf-8') as f:
            contents = f.read()
            num = contents.lower().count('the ')
            print(f"'The' appears {num} times in {book}.")
    except FileNotFoundError:
        pass