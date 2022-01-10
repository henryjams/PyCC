# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 21:25:27 2021

@author: Hank
"""

results = {}

polling = "active"

while polling == "active":
    respondent = input("Please input your name:\n")
    vacation = input("What is your ideal vacation spot:\n")
    
    results[respondent] = vacation
    
    again = input("Is there another respondent? (yes/no)")
    if again == 'no':
        polling = "inactive"
        
for respondent, vacation in results.items():
    print(f"{respondent.title()} would like to travel to {vacation.title()}.")