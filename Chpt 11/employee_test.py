# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 14:57:28 2022

@author: Hank
"""

import unittest
from employee import Employee

class TestEmployeeClass(unittest.TestCase):
    """Tests the employee class"""
    
    def setUp(self):
        """create a sample employee for the purposes of testing"""
        self.frank = Employee('Frank', 'Josen', 48000)
        
    def test_standard_raise(self):
        """test standard raise"""
        self.frank.give_raise()
        self.assertEqual(self.frank.salary, 53000)
    
    def test_custom_raise(self):
        """test custom raise"""
        self.frank.give_raise(7500)
        self.assertEqual(self.frank.salary, 55500)
    
if __name__ == '__main__':
    unittest.main()