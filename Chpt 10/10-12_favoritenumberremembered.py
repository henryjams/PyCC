# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 20:05:15 2022

@author: Hank
"""

import json

file_name = 'fav_num.json'

try:
    with open(file_name) as f:
        fav_num = json.load(f)
except:
    fav_num = input("Tell me your favorite number: \n")
    with open(file_name, 'w') as f:
        json.dump(fav_num, f)
else:
    print(f"Your favorite number is {fav_num}!")