#! /usr/bin/env python3
# COMMENTS for DEVELOPERS/CODERS
# Author: DCameron
# Description: This script will demo HOWTO define a VARIADIC function
# which is a function that accepts variable number of parameters!
"""
    This module has several functions for searching for
    Regex patterns in one or more file/s
"""
import re

# Example of a VARIADIC function which unpacks
# all remaining parameters into a TUPLE
def search_pattern(pattern=r"^.{19}$", *files):
    """ Search for Regex patterns in file/s and return num
        lines matched
    """
    lines = 0
    for file in files:
        fh_words = open(file, mode="rt")

        for line in fh_words:
            m = re.search(pattern, line)  # Match pattern
            if m:
                lines += 1
                print(line, end="")

        fh_words.close() # Close file handle
    return lines

num_lines = search_pattern(r"^([A-Z]).*\1$", r"f:\labs\words", r"f:\labs\words2", r"F:\labs\words3")
print(f"Matched {num_lines} lines")
