#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO create, and grow,
# and shrink, and access dictionaries = UNORDERED Collection
# with Unique keys. From Py 3.6 onwards they are in INSERTION ORDER
""" 
    DocString
"""
import pprint

# Created a multi-dimensional dict of lists
movies = { 'joe': ['underworld', 'blade', 'twilight'],
           'brianna': ['the notebook', 'inside out',  'the gentleman'],
           'dayane': ['iron man', 'transformers', 'resident evil']
}

# Grow a dict..
movies['donald'] = ['lotr', 'the hobbit', 'Mission Impossible']
movies['zac'] = ['the creator', 'star wars', 'black cauldron']

# Access values from inside dict...
print(f"Brianna's favourite movies = {movies.get("brianna")}")
print(f"Brianna's favourite movies = {movies['brianna']}")
print(f"Brianna's ultimate movie = {movies['brianna'][0]}")

# Shrink a dict...
movies.pop('dayane') # Remove Key+Value
movies.popitem() # Remove LAST INSERTED key+value

# Other methods..
films = movies.copy() # Copy dict
films.clear() # Empty list

print("-" * 60)
# Display entire dict in human readable format
pprint.pprint(movies)

print("-" * 60)
# ITERATE through a dict keys using the .keys() method
for name in movies.keys():
    print(f"{name} likes the movies {movies[name]}")

# ITERATE through a dict VALUES using the .values() method
for films in movies.values():
    print(f"Recommend films = {films}")

# ITERATE through a dict KEYS+VALUES using the .items() method
for (name, films) in movies.items():
    print(f"{name} loves the films {films}")