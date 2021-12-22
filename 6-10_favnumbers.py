# -*- coding: utf-8 -*-
"""
Created on Thu May 27 17:26:29 2021

@author: Hank
"""

fav_num = {
    'marshall': [3,5,11],
    'aaron':[2,3,4],
    'sam': [9,10,11,800],
    'proZD': [1400,1401],
    'jess': [9,45,60],
    }

for name, nums in fav_num.items():
    print(f"\nMy friend {name.title()}'s favorite numbers are:")
    for num in nums:
        print("\t" + str(num))