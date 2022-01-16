# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 22:01:52 2022

@author: Hank
"""

def city_namer(city, country, pop = 0):
    """take the name of a city and country and format it"""
    if pop:
        city_name = f"{city.title()}, {country.title()} - population {pop}"
    else:
        city_name = f"{city.title()}, {country.title()}"
    return city_name

print("Thank you for using city name formatter.")
print("    Press q at any time to quit.")

while True:
    city = input("Please enter the name of the city: ")
    if city == 'q':
        break
    country = input("Please enter the name of the country: ")
    if country == 'q':
        break
    pop = input("Please enter the population: ")
    if pop == 'q':
        break
    
    formatted_city_name = city_namer(city, country, pop)
    print(f"\nFormatted city name: \n    {formatted_city_name}")