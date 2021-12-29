# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 10:55:32 2021

@author: Hank
"""

# Adding this comment to test a push to github via git

class Users:
    """user info etc"""
    
    def __init__(self, first_name, last_name, age, height, weight):
        """method to store user information"""
        self.fname = first_name
        self.surname = last_name
        self.age = age
        self.height = height
        self.weight = weight
        self.login_attempts = 0
                
    def describe_user(self):
        print(f"\n{self.fname.title()} {self.surname.title()}")
        print(f"Age : {self.age}")
        print(f"Height : {self.height}")
        print(f"Weight : {self.weight}")
        print(f"{self.login_attempts}")
        
    def greet_user(self):
        print(f"\nGreetings {self.fname.title()} {self.surname.title()}.")
        
    def increment_login_attempts(self):
        """method to add to the login attempts count"""
        self.login_attempts += 1
                
    def reset_login_attempts(self):
        """resets login attempt count"""
        if self.login_attempts == 0:
            print("This user has not attempted to login.")
        else:
            self.login_attempts = 0
        
#Paul instance        
paul = Users('paul', 'veerhoven', 32, 66, 210)
paul.describe_user()
paul.greet_user()

#Dolly instance
dolly = Users('dolly', 'the great', 700, 'yes', 110)
dolly.describe_user()
dolly.greet_user()

dolly.increment_login_attempts()
dolly.increment_login_attempts()
dolly.increment_login_attempts()

dolly.describe_user()

dolly.reset_login_attempts()

dolly.describe_user()