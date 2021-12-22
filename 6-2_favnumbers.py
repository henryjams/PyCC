# -*- coding: utf-8 -*-
"""
Created on Thu May 27 17:26:29 2021

@author: Hank
"""

fav_num = {
    'marshall':'3',
    'aaron':'0',
    'sam':'800',
    'proZD':'1400',
    'jess':'9'
    }

for name, num in fav_num.items():
    print(f"\nMy friend {name.title()}'s favorite number is {num}")