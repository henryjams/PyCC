# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 10:27:18 2021

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

class IceCreamStand(Restaurant):
    """to make an ice cream stand"""
    
    def __init__(self, name, cuisine):
        """this method defines the attributes to the ice cream stand"""
        super().__init__(name, cuisine)
        self.flavors = []
        
    def list_flavors(self):
        """display the flavors assigned to the ice cream stand class"""
        print(f"The flavors featured at {self.name} are:")
        for flavor in self.flavors:
            print(f"  ~ {flavor.title()}")

# olio section            
olio = Restaurant('olio', 'italian')

print(olio.name)
print(olio.cuisine,"\n")

olio.describe_restaurant()
olio.open_restaurant()

# sundae section
sundae = IceCreamStand('Sundae Best', 'Ice Cream')
sundae.flavors = ['Cherry', 'Chocolate', 'Mint']

print(sundae.name)

sundae.list_flavors()
sundae.open_restaurant()

