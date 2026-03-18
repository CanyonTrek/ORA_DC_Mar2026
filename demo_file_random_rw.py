#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO open, and close,
# and read/write RANDOMLY to a text/binary file using the
# the .seek() and .tell() methods.
"""
    DocString
"""

movies = { 'joe': ['underworld', 'blade', 'twilight'],
           'brianna': ['the notebook', 'inside out',  'the gentleman'],
           'dayane': ['iron man', 'transformers', 'resident evil'],
           'zac': ['the creator', 'star wars', 'black cauldron']
}
# Open file handle for READING in TEXT mode
with open(r"f:\labs\projects\ORA_DC_Mar2026\movies.txt", mode="rt") as fh_in:
    fh_in.seek(90, 0) # Seek forwards 90 chars from SOF
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

    fh_in.seek(135, 0) # Seek forwards 135 chars from SOF
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

print("=" * 60)

# Open file handle for READING in BINARY mode
with open(r"f:\labs\projects\ORA_DC_Mar2026\movies.txt", mode="rb") as fh_in:
    fh_in.seek(-60, 2) # Seek back 60 bytes from EOF
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

    fh_in.seek(-55, 1) # Seek back 55 bytes current position
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

