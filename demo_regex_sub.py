#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO MATCH and SUBSTITUTE
# strings using the re module
""" 
    DocString
"""
import re

# Sample line from /etc/passwd on Linux for root user account
line = "root:x:0:0:The Super User:/root:/bin/ksh"

line = re.sub(r"[Ss]uper [Uu]ser", r"Administrator", line) # Returns a modified str
(line, num) = re.subn(r"ksh$", r"bash", line) # Returns a tuple (modified str, num)

print(f"Modified line = {line} with {num} changes")