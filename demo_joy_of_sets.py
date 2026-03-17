#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO create, and grow, and
# shrink and COMBINE sets. SET is UNORDERED Collection of Unique
# values.
""" 
    DocString
"""
marvel_fans = {'celso', 'savita', 'rafael', 'sofia', 'donald'}
dc_fans = set() # Create an empty SET

# Grow a set..
dc_fans.add('donald')
dc_fans.add('sharath')
dc_fans.add('zac')

# Shrink a set..
# dc_fans.pop() # Remove a random value
comic_fans = dc_fans.copy() # Copies SET
comic_fans.clear() # Empty SET

print(f"Fans of Marvel = {marvel_fans}")
print(f"Fans of DC = {dc_fans}")

# COMBINE SETS using SET methods (Remember VENN diagrams)
print(f"Fans of either Marvel OR DC = {marvel_fans.union(dc_fans)}")
print(f"Fans of both Marvel AND DC = {marvel_fans.intersection(dc_fans)}")
print(f"Fans of ONLY Marvel = {marvel_fans.difference(dc_fans)}")
print(f"Fans of either Marvel OR DC = {marvel_fans.symmetric_difference(dc_fans)}")
print("-" * 60)
# COMBINE SETS using SET operators (Remember VENN diagrams)
print(f"Fans of either Marvel OR DC = {marvel_fans | dc_fans}")
print(f"Fans of both Marvel AND DC = {marvel_fans & dc_fans}")
print(f"Fans of ONLY Marvel = {marvel_fans - dc_fans}")
print(f"Fans of either Marvel OR DC = {marvel_fans ^ dc_fans}")

