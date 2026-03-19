#! /usr/bin/env python3
# Author: DCameron
# Description: This module will define several advanced calculator
# functions for a calculator app
""" 
    Calc App with advanced power, modulus and square root functions
"""

def power(x, z):
    """ Return x to the power z as a float """
    return float(x**z)

def mod(x, z):
    """ Return REMAINDER after x divided by z as a float """
    return float(x % z)

def sqrt(x):
    """ Square root of x to 3 decimal places """
    return round(x**0.5, 3)


print("----------- Adv Calc App------------")
print(f"9 ** 8 = {power(9, 8)}")
print(f"99 % 88 = {mod(99, 88)}")
print(f"\N{square root}99 = {sqrt(99)}")
print("------------------------------------")