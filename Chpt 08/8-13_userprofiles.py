# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 16:55:55 2021

@author: Hank
"""

def build_profiles(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profiles('hank', 'sparkles', 
                              job='nuthing', location='nola')

print(user_profile)