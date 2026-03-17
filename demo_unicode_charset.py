#! /usr/bin/env python3
# Author: DCameron
# Description: This script will display the entire Unicode
# charset
""" 
    DocString
"""

# Iterate through the the unicode chars from 0->65535
for pos in range(0, 65536):
    try:
        print(chr(pos), end=" ")
        if pos % 16 == 0:
            print()
    except UnicodeEncodeError:
        print(" ")