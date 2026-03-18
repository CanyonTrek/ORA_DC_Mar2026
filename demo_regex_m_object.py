#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO Match text data
# from text files using str matching and PATTERN matching with the
# re module.
"""
    DocString
"""
import re

# Open file for READING in Text mode
fh_words = open(r"f:\labs\words", mode="rt")

reobj = re.compile(r"^(.)(.).\2\1$") # PRE-COMPILE pattern ONLY ONCE!

for line in fh_words:
    m = reobj.search(line)  # Match 5 char palindromes
    if m:
        print(f"Matched {m.group()} on line {line.rstrip()} at {m.start()}-{m.end()},"
              f"Groupings={m.groups()}, Group 1 = {m.group(1)}")

fh_words.close() # Close file handle
