#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO ITERATOR through
# a SEQUENCE (str/tuple/list/dict/sets) using an ITERATOR for
# loop
""" 
    DocString
"""
import sys
from tkinter.ttk import Label

#               0          1         2       3         4        5
students = ['brianna', 'sharath', 'john', 'savita', 'celso', 'sofia']

# ITERATE through the student using an
# ITERATOR for loop
for name in students:
    print(name, end="\n")
print("Students: ", students)

# ITERATE through the students and modify the names using an
# ITERATOR for loop
idx = 0
for name in students:
    print(name.upper(), end="\n")
    students[idx] = name.upper()
    idx += 1
print("Students: ", students)

# ITERATE through the students and modify the names using an
# ITERATOR for loop plus the built-in enumerate() function
for (idx, name) in enumerate(students, start=0):
    print(name.title(), end="\n")
    students[idx] = name.title()
print("Students: ", students)

try:
    sys.exit(10) # Explicit EXIT with return code (0=success, 1-255=error)
    # sys.exit("Goodbye") # Explicit EXIT (message-> STDERR) + code of 1
except SystemExit:
    print("exiting..")
    sys.exit(0)