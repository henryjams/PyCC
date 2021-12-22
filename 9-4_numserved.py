# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21

@author: Hank
"""

class Restaurant:
    """to make restaurant"""
    
    def __init__(self, name, cuisine):
        """this method gives basic descriptions of the restaurant"""
        self.name = name.title()
        self.cuisine = cuisine
        self.customers_served = 0
        
    def describe_restaurant(self):
        """prints out the description we give the class"""
        print(f"This restaurant is called {self.name}.")
        print(f"{self.name} serves {self.cuisine}.")
        print(f"{olio.name} has served {olio.customers_served} " 
              "customers so far.\n")
        
    def open_restaurant(self):
        """opens the restaurant"""
        print(f"{self.name} is now open!\n")
        
    def count_customers(self, customers):
        """adds the number of customers to the count"""
        self.customers_served += customers
        
olio = Restaurant('olio', 'italian')

olio.describe_restaurant()
olio.open_restaurant()

olio.count_customers(100)

olio.describe_restaurant()