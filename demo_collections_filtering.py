#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO COPY and OPTIONALLY
# Filter collections (str/tuple/list/dict/set)
""" 
    DocString
"""

students = ['rafael', 'joe', 'shrath', 'sumkanth', 'savita',
            'celso', 'sofia', 'brianna', 'john', 'joe']

# Copy list and optionally filter the values using
# 1.Iterator Loop + collection, optional condition, expression
wee_names = []
for name in students: # 1.Iterator + source collection
    if len(name) <= 5: # 2.Optional condition (filtering)
        wee_names.append(name.upper()) # 3.Expression
print(f"1.Short names = {wee_names}")

# 2.Iterator Loop + collection, user functions (filtering), expression
def filter_names(name):
    """ Return True if name <= 5 chars in length """
    if len(name) <= 5:
        return True
    else:
        return False

wee_names = []
for name in students: # 1.Iterator + source collection
    if filter_names(name): # 2.Optional condition (filtering)
        wee_names.append(name.upper()) # 3.Expression
print(f"2.Short names = {wee_names}")

# 3.Built-in filter function (iterating), user functions (filtering).
wee_names = list(filter(filter_names, students))
print(f"3.Short names = {wee_names}")

# 4.Built-in filter function (iterating), lambda functions (filtering).
wee_names = list(filter(lambda name:len(name) <= 5, students))
print(f"4.Short names = {wee_names}")

# 5.LIST Comprehension [ expr, for loop + source, optional condition ]
wee_names = [ name.upper() for name in students if len(name) <= 5 ]
print(f"5.Short names = {wee_names}")

# 5.1.LIST Comprehension [ expr, for loop + source, optional condition ]
wee_names = [ (name.upper(), len(name)) for name in students if len(name) <= 5 ]
print(f"5.1.Short names = {wee_names}")

# 5.2.DICT Comprehension [ expr, for loop + source, optional condition ]
# Dict have unique keys: So DUPLICATE keys have been filtered out!
wee_names = { name.upper(): len(name) for name in students if len(name) <= 5 }
print(f"5.2.Short names = {wee_names}")

# 5.3.SET Comprehension [ expr, for loop + source, optional condition ]
# SETS have unique VALUES: So DUPLICATE values have been filtered out!
wee_names = { name.upper() for name in students if len(name) <= 5 }
print(f"5.3.Short names = {wee_names}")