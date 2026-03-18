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
    # m = re.search(r"^(.)(.).\2\1$", line)  # Match 5 char palindromes
    m = reobj.search(line)  # Match 5 char palindromes
    if m:
        print(line, end="")

fh_words.close() # Close file handle