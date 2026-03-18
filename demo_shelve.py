#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO 
""" 
    DocString
"""
import shelve
movies = { 'joe': ['underworld', 'blade', 'twilight'],
           'brianna': ['the notebook', 'inside out',  'the gentleman'],
           'dayane': ['iron man', 'transformers', 'resident evil'],
}
tv_series = { 'joe': ['buffy', 'angel'],
              'brianna': ['ted lasso', 'parks and rec'],
              'bogdan': ['breaking bad', 'prison break'],
}
books = { 'joe': 'dummies guide to python',
          'brianna': 'harry potter',
          'bogdan': 'america',
}

with shelve.open(r"f:\labs\projects\ORA_DC_Mar2026\media") as db:
    db['movies'] = movies
    db['tv_series'] = tv_series
    db['books'] = books

with shelve.open(r"f:\labs\projects\ORA_DC_Mar2026\media") as db:
    print(f"Joe's favourite movies are {db['movies']['joe']}")
    print(f"Brianna's favourite tv_series is {db['tv_series']['brianna'][0]}")
    print(f"Bogdan's favourite book is {db['books']['bogdan']}")
