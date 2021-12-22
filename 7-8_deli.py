# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 20:54:36 2021

@author: Hank
"""

sandwich_orders = ['italian','meatball','turkey','chicken pesto']
finished_sandos = []

while sandwich_orders:
    working_sando = sandwich_orders.pop()
    
    print(f"Making sando: {working_sando.title()} sando.")
    finished_sandos.append(working_sando)

print()
for sando in finished_sandos:
    print(f"A delicious {sando.title()} sando was made this day.")
    