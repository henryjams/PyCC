# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 20:02:31 2022

@author: Hank
"""

import json

file_name = 'fav_num.json'

with open(file_name, 'r') as f:
    contents = json.load(f)
    
print(f"Your favorite number is {contents}!")