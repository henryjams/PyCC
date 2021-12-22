# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 21:11:44 2021

@author: Hank
"""

sandwich_orders = [
    'italian','meatball','turkey','chicken pesto',
    'pastrami','pastrami','pastrami']
finished_sandos = []

print("We are out of pastrami sry\n")

while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    working_sando = sandwich_orders.pop()
    
    print(f"Making sando: {working_sando.title()} sando.")
    finished_sandos.append(working_sando)

print()
for sando in finished_sandos:
    print(f"A delicious {sando.title()} sando was made this day.")
    