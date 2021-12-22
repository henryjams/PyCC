# -*- coding: utf-8 -*-
"""
Created on Thu May 27 17:43:53 2021

@author: Hank
"""

cities = {
    'Rome':{
        'country':'Italia',
        'population':'2.873 million',
        'info':'The Eternal City'
        },
    'Nashville':{
        'country':'USA',
        'population':'697,280',
        'info':'Music City'
        },
    'New Orleans':{
        'country':'USA',
        'population':'390,845',
        'info':'The Crescent City'
        }
    }

for city, details in cities.items():
    print("\n" + city)
    for detail, info in details.items():
        print("\t" + detail.title() + ": " + info)