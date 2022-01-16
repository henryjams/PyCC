# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 10:55:13 2022

@author: Hank
"""

class Employee:
    """describe an employee"""
    
    def __init__(self, first, last, salary):
        """descriptors of employee"""
        self.first_name = first.title()
        self.last_name = last.title()
        self.salary = salary
        
    def give_raise(self, raise_amount = 5000):
        """gives a raise to employee"""
        self.salary += raise_amount
        return self.salary

frank = Employee('Frank', 'Josen', 48000)
    
frank.give_raise()