# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 10:55:32 2021

@author: Hank
"""

class Users:
    """user info etc"""
    
    def __init__(self, first_name, last_name, age, height, weight):
        """method to store user information"""
        self.fname = first_name
        self.surname = last_name
        self.age = age
        self.height = height
        self.weight = weight
                
    def describe_user(self):
        print(f"\n{self.fname.title()} {self.surname.title()}")
        print(f"Age : {self.age}")
        print(f"Height : {self.height}")
        print(f"Weight : {self.weight}")
        
    def greet_user(self):
        print(f"\nGreetings {self.fname.title()} {self.surname.title()}.")

#Paul instance        
paul = Users('paul', 'veerhoven', 32, 66, 210)
paul.describe_user()
paul.greet_user()

#Dolly instance
dolly = Users('dolly', 'the great', 700, 'yes', 110)
dolly.describe_user()
dolly.greet_user()