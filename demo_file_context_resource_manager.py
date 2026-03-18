#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO open, a text file for
# reading, writing, or appending, and then closing the file handle
"""
    DocString
"""

movies = { 'joe': ['underworld', 'blade', 'twilight'],
           'brianna': ['the notebook', 'inside out',  'the gentleman'],
           'dayane': ['iron man', 'transformers', 'resident evil'],
           'zac': ['the creator', 'star wars', 'black cauldron']
}

with open(r"f:\labs\projects\ORA_DC_Mar2026\movies.txt", mode="wt") as fh_out:
    for name in movies.keys():
        print(f"{name} {movies[name]}", end="\n")
        fh_out.write(f"{name} {movies[name]}\n")
    # End of Block

print("=" * 60)

with open(r"f:\labs\projects\ORA_DC_Mar2026\movies.txt", mode="rt") as fh_in:
    for line in fh_in:
        print(line, end="")
    # End of block, File handle is closed
