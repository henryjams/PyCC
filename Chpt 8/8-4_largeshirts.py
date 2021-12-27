# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 20:42:19 2021

@author: Hank
"""

def make_shirt(size = 'large', msg = 'i love python'):
    print(
    f"The shirt is size {size}, and should be printed with '{msg}' on it.")
    
make_shirt()
make_shirt('medium')
make_shirt('small', msg = 'yo stinky!')

