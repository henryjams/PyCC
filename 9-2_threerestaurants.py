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

#Olio instance
print()
olio = Restaurant('olio', 'italian')

olio.describe_restaurant()
olio.open_restaurant()

#Pepper and Pie
print()
pepper_pie = Restaurant('Pepper and Pie', 'Chicken and Pie')

pepper_pie.describe_restaurant()
pepper_pie.open_restaurant()

#Origin
print()
origin = Restaurant('origin', 'seafood')

origin.describe_restaurant()
origin.open_restaurant()