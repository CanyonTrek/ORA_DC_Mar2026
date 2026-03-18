#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO open, a text file for
# reading, writing, or appending, and then closing the file handle
""" 
    DocString
"""
import sys
movies = { 'joe': ['underworld', 'blade', 'twilight'],
           'brianna': ['the notebook', 'inside out',  'the gentleman'],
           'dayane': ['iron man', 'transformers', 'resident evil'],
           'zac': ['the creator', 'star wars', 'black cauldron']
}
# Open file handle for WRITING in TEXT mode
fh_out = open(r"f:\labs\projects\ORA_DC_Mar2026\movies.txt", mode="wt")

# Iterate through the dict keys and write movie info to file
for name in movies.keys():
    print(f"{name} {movies[name]}", end="\n", file=sys.stdout)
    print(f"{name} {movies[name]}", end="\n", file=fh_out)
    #fh_out.write(f"{name} {movies[name]}\n")

# fh_out.flush() # Flush buffers
fh_out.close() # Flush buffers and close file handle

print("=" * 60)

# Open file handle for READING in TEXT mode
fh_in = open(r"f:\labs\projects\ORA_DC_Mar2026\movies.txt", mode="rt")

# text = fh_in.read() # Read ENTIRE file into str object! Be Careful!
# text = fh_in.read(30) # Read NEXT 30 chars into str object
# text = fh_in.readline() # Read NEXT LINE into str object.
# lines = fh_in.readlines() # Read ENTIRE file into a LIST object, Be Careful!
# print(f"1st line is {lines[0]}")
# print(f"Last line is {lines[-1]}")

# ITERATE through a file handle one line at a time
# Iterator for loop plus Iterator Object (next/iter)
# for line in open(r"f:\labs\projects\ORA_DC_Mar2026\movies.txt", mode="rt"):
for line in fh_in:
    print(line, end="")

fh_in.close() # Close file handle