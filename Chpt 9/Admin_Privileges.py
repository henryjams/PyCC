# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 17:41:26 2022

@author: Hank

This file contains the modules for creating Admin users and assigning
their privilges. It has dependencies on the User_v2 module.

"""

from User_v2 import Users

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