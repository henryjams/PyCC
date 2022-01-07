# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 17:21:12 2022

@author: Hank
"""

from User_v2 import Users
from Admin_Privileges import Privileges
from Admin_Privileges import Admin

Max = Admin('Max', 'Power', 29, 77, 205)

max_privileges = [
    'do all the things',
    'delete user info',
    'crunch on chips'
    ]

Max.privileges.privileges = max_privileges

Max.describe_user()
Max.privileges.show_privileges()
Max.greet_user()