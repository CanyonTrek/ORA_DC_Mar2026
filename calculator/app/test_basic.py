#! /usr/bin/env python3
# Author: DCameron
# Description: This script defines TEST Cases for the basic module
""" 
    ONLY Reports on FIRST ERROR!
"""
import basic

def test_add():
    assert basic.add(4, 3, 2, 1) == 10.0, "Should be 10.0"
    assert basic.add(30, 20) == 50.0, "Should be 50.0"
    return None

def test_mul():
    assert basic.mul(4, 3, 2) == 24.0, "Should be 24.0"
    return None

def test_div():
    assert basic.div(4, 3) == 1.333, "Should be 1.333"
    return None

def main():
    print("Starting Tests 3..2..1..")
    test_add()
    test_mul()
    test_div()
    print("All TESTS successful!")
    return None

if __name__ == "__main__":
    main()