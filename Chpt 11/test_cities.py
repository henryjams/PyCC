# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 22:24:04 2022

@author: Hank
"""

import unittest
from cityfunctions import city_namer

class NamerTestCase(unittest.TestCase):
    """test the city_namer function"""
    
    def test_city_country(self):
        formatted_name = city_namer('rome', 'italy')
        self.assertEqual(formatted_name, 'Rome, Italy')
    
    def test_city_country_pop(self):
        formatted_name = city_namer('rome', 'italy', pop = 4_000_000)
        self.assertEqual(formatted_name, 'Rome, Italy - population 4000000')
    
if __name__ == '__main__':
    unittest.main()