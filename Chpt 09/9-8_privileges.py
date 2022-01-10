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
        self.login_attempts = 0
                
    def describe_user(self):
        print(f"{self.fname.title()} {self.surname.title()}")
        print(f"Age : {self.age}")
        print(f"Height : {self.height}")
        print(f"Weight : {self.weight}")
        print(f"{self.login_attempts}")
        
    def greet_user(self):
        print(f"\nGreetings {self.fname.title()} {self.surname.title()}.\n")
        
    def increment_login_attempts(self):
        """method to add to the login attempts count"""
        self.login_attempts += 1
                
    def reset_login_attempts(self):
        """resets login attempt count"""
        if self.login_attempts == 0:
            print("This user has not attempted to login.")
        else:
            self.login_attempts = 0

class Admin(Users):
    """admin class"""
    
    def __init__(self, first_name, last_name, age, height, weight):
        super().__init__(first_name, last_name, age, height, weight)
        self.privileges = Privileges()
        
class Privileges:
    """Stores admin privileges"""
    
    def __init__(self, privileges=[]):
        self.privileges = privileges
        
    def show_privileges(self):
        print("The admin has the following privileges:")
        for privilege in self.privileges:
            print(f" - {privilege}")
             
# Admin instance
admin = Admin('john', 'doe', 50, 72, 180)
admin_privileges = [
    'edit user records',
    'print out user records',
    'have fun'
    ]

admin.privileges.privileges = admin_privileges
admin.privileges.show_privileges()
admin.greet_user()