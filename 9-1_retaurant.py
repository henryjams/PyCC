# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 10:27:18 2021

@author: Hank
"""

class Restaurant:
    """to make restaurant"""
    
    def __init__(self, name, cuisine):
        """this method gives basic descriptions of the restaurant"""
        self.name = name
        self.cuisine = cuisine
        
    def describe_restaurant(self):
        """prints out the description we give the class"""
        print(f"This restaurant is called {self.name.title()}.")
        print(f"{self.name.title()} serves {self.cuisine}.")
        
    def open_restaurant(self):
        """opens the restaurant"""
        print(f"{self.name.title()} is now open!")

olio = Restaurant('olio', 'italian')

print(olio.name)
print(olio.cuisine,"\n")

olio.describe_restaurant()
olio.open_restaurant()