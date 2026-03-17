#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO repeat a BLOCK of
# commands a specific number of times using COUNTER loop.
""" 
    DocString
"""

count = 0 # 1.Initialise counter START
while count < 10: # 2.Test counter STOP
    print(count)
    count += 1 # 3.Increment counter STEP

# Alternatively, we could use an ITERATOR for loop
# plus the built-in range(start, stop, step) function
for num in range(0, 10, 1):
    print(num)

# plus the built-in range(start, stop, step=1) function
for num in range(0, 10):
    print(num)

# plus the built-in range(start=0, stop, step=1) function
for num in range(10):
    print(num)