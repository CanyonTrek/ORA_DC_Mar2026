#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO CHECK which platform
# your script is running on!
""" 
    DocString
"""
import sys
import os

if sys.platform == "win32":
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

print("My home directory is", hdir)