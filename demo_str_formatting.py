#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO format strings
# using several different techniques
""" 
    DocString
"""
# Dict of planets and their distance to the sun in Giga metres
planets = {'Mercury': 57.91,
           'Venus': 108.2,
           'Earth': 149.597870,
           'Mars': 227.94
}

# Iterate through planet keys and display planet info
# using escape chars and str concatenation - UGLY
for planet in planets.keys():
    print("\t\t" + planet + ": " + str(planets[planet]) + " Gm")

print("-" * 40)
# using str justification methods and concatenation - OK
for planet in planets.keys():
    print(planet.rjust(12) + ": " + str(planets[planet]).rjust(12, '.') + " Gm")

print("-" * 40)
# using str.format() method - Good! Python 3 onwards
for planet in planets.keys():
    print("{0:>12s}: {1:.>12.3f} Gm ".format(planet, planets[planet]))

print("-" * 40)
# using f-strings - My favourite! Python 3.5 onwards
for planet in planets.keys():
    print(f"{planet:>12s}: {planets[planet]:.>12.3f} Gm ")