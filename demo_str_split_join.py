#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO split and rejoin
# strings using the str.split() and str.join() methods
""" 
    DocString
"""

# Sample line from /etc/passwd on Linux for root user account
line = "root:x:0:0:The Super User:/root:/bin/ksh"

# BUT I want to make changes in the str! str=immutable!
fields = line.split(":") # Return a list! list=mutable!
fields[4] = "The Administrator"
fields[6] = "/bin/bash"

line = ":".join(fields) # Returns a NEW str object
print(line)
