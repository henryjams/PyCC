# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 08:44:48 2021

@author: Hank
"""

def order(*items):
    print("Here are the toppings for the sandwich:")
    for item in items:
        print(f"- {item}")
        
order('boba')
order('boba', 'pizza', 'ice cream')
order('sandwich', 'boba')
