# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 19:57:44 2022

@author: Hank
"""

import json

fav_num = input("Tell me your favorite number: \n")

file_name = 'fav_num.json'

with open(file_name, 'w') as f:
    json.dump(fav_num, f)