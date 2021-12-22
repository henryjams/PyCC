# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 20:47:19 2021

@author: Hank
"""

def describe_city(name, country = 'Italy'):
    print(f"{name.title()} is in {country.title()}.")
    
describe_city('rome')
describe_city('sienna')
describe_city('madrid', 'spain')