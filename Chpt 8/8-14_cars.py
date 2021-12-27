# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 17:13:57 2021

@author: Hank
"""

def car_profile(make, model, **car_info):
    """
    
    Parameters
    ----------
    make : TYPE
        DESCRIPTION.
    model : TYPE
        DESCRIPTION.
    **car_info : TYPE
        DESCRIPTION.

    Returns
    -------
    car_info : TYPE
        DESCRIPTION.

    """
    car_info['manufacturer'] = make
    car_info['model'] = model
    return car_info

car_facts = car_profile('honda', 'odyssey', color='steel', engine='Yuge')

print(car_facts)