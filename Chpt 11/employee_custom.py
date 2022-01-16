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
        
    def give_raise(self):
        """gives a raise to employee"""
        raise_type = input("Is this a standard raise? (y/n) ")
        if raise_type == 'y':
            self.salary = int(self.salary) + 5000
        elif raise_type == 'n':
            raise_amount = input("Please enter raise amount: ")
            self.salary = int(self.salary) + int(raise_amount)
        else:
            print("Answer invalid.")
        salary_message = (f"{self.first_name.title()}'s salary ")
        salary_message += (f"is now {self.salary}.")
        print(salary_message)
        return self.salary    
            
frank = Employee('Frank', 'Josen', 48000)
    
frank.give_raise()