#! /usr/bin/env python3
# Author: DCameron
# Description: This is a Calculator App with Basic and Advanced
# features
""" 
    Calculator App with Basic and Advanced functions
"""
import sys
# Next two imports IMPORT into your __main__ namespace!!!!!
# from app.basic import add, mul, div # Can Create Namespace Pollution
# from app.basic import * # UNSAFE

from app import basic
from app import adv
# import app.basic as basic # Import and rename NameSpace as basic.
# import app.adv as adv

def main():
    menu = """
        Menu Options
        ------------
        1.Display Basic features
        2.Display Adv features
        q.Quit
    """

    while True:
        print(menu)
        option = input("Enter option (1-2,q=quit): ")

        if option == "1":
            print(f"20 + 19 + 18 = {basic.add(20, 19, 18)}")
            print(f"20 * 19 * 18 = {basic.mul(20, 19, 18)}")
            print(f"20 / 19 = {basic.div(20, 19)}")
        elif option == "2":
            print(f"20 ** 19 = {adv.power(20, 19)}")
            print(f"20 % 18 = {adv.mod(20, 18)}")
            print(f"\N{square root}20 = {adv.sqrt(20)}")
        elif option == "q":
            print("Quitting..")
            break
        else:
            print("Invalid option")
    return None

# Namespace Trick
if __name__ == "__main__":
    # Execute if RAN DIRECTLY as a program
    # Ignored if imported as a module
    main()
    sys.exit(0) # Explicit EXIT with error code
