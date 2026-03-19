#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO generate collections
# in a more memory efficient way using a generator function and
# the YIELD statement
""" 
    DocString
"""

def get_numbers():
    """ Return an ENTIRE list of numbers """
    numbers = []
    for x in range(0, 10000000000000):
        numbers.append(x)
    return numbers

def generate_numbers():
    """ YIELD one object from the collection at a time """
    for x in range(0, 10):
        yield x

# for z in get_numbers():
for z in generate_numbers():
    print(z)

print("-" * 50)
# Alternative to using a for loop..
gen = generate_numbers()
while True:
    num = next(gen, -1)
    if num != -1:
        print(num)
    else:
        break