#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO generate 6
# random UNIQUE numbers
""" 
    DocString
"""
import random

lotto = [] # Create empty list to store lottery numbers

# Repeat whilst condition remains True
while len(lotto) < 6:
    num = random.randint(1, 50)
    if num not in lotto:
        lotto.append(num)
    else:
        print("Duplicate number:", num)


print("lottery numbers =", lotto)