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

# Iterate through the file using Iterator for loop
for line in fh_words:
    # Example of str testing
    # if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
    # m = re.search(r"the", line) # Match lines with 'the'
    # m = re.search(r"^the", line)  # Match lines STARTING with 'the'
    # m = re.search(r"ing$", line)  # Match lines ENDING with 'ing'
    # m = re.search(r"^.ing$", line)  # Match lines of 4 chars ENDING with 'ing'
    # m = re.search(r"^[adzp]ing$", line)  # Match lines of 4 chars ENDING with 'ing'
    # m = re.search(r"^...................$", line)  # Match lines of EXACTLY 19 chars
    # m = re.search(r"^.{19}$", line)  # Match lines of EXACTLY 19 chars
    # m = re.search(r"^[A-Z]", line)  # Match lines START with a CAPITAL
    # m = re.search(r"\.", line)  # Match lines with a DOT using ESCAPE char
    # m = re.search(r"[.]", line)  # Match lines with a DOT using ESCAPE char
    # m = re.search(r"^[A-Z].*[A-Z]$", line)  # Match lines start/end with a CAPITAL
    # m = re.search(r"[aeiou]{5,}", line)  # Match lines with at least 5 consecutive vowels
    # m = re.search(r"^(.)(.).\2\1$", line)  # Match lines with 5 char palindromes
    # m = re.search(r"^([A-Z]).*\1$", line)  # Match lines start/end with SAME CAPITAL
    # m = re.search(r"banana|pineapple|orange", line)  # Match pat1 OR pat2 OR pat3
    # m = re.match(r"(.)(.).\2\1$", line)  # Match - AUTO matches START of LINE
    m = re.fullmatch(r"^(.)(.).\2\1$\n", line)  # Match ENTIRE LINE incl SILENT Chars
    if m:
        print(line, end="")

fh_words.close() # Close file handle