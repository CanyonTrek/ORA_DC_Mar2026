#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO define a user function
# with optional parameters passing, optional default values and
# optional return value.
"""
    DocString
"""
import re

def search_pattern(pattern=r"^.{19}$", file=r"f:\labs\words"):
    lines = 0
    fh_words = open(file, mode="rt")

    for line in fh_words:
        m = re.search(pattern, line)  # Match pattern
        if m:
            lines += 1
            print(line, end="")

    fh_words.close() # Close file handle
    return lines

search_pattern()
num_lines = search_pattern(r"^([A-Z]).*\1$", r"f:\labs\words")
print(f"Matched {num_lines} lines")