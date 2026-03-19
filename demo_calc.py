#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO define, name and call
# a user function with optional parameter passing and documentation
""" 
    Calculator App with Add, multiply and divide functions
"""

def add(x, z):
    """ Return SUM of x and z as a float """
    return float(x + z)

def mul(x, z):
    """ Return PRODUCT of x and z as a float """
    return float(x * z)

def div(x, z):
    """ Return QUOTIENT of x divided by z to 3 decimal places """
    return round(x/z, 3)

print(f"4 + 3 = {add(4, 3)}")
print(f"4 * 3 = {mul(4, 3)}")
print(f"4 / 3 = {div(4, 3)}")

# Alternatively, we could DEFINE a SIMPLE user
# function which is used sparingly without using the
# def statement

l_add = lambda x, z:float(x + z)
print(f"4 + 3 = {l_add(4, 3)}")

print(f"4 + 3 = {(lambda x,z:float(x + z))(4, 3)}")