#! /usr/bin/env python3
# Author: DCameron
# Description: This is a Calculator App with Basic and Advanced
# features
""" 
    Calculator App with Basic and Advanced functions
"""
import sys
from app import basic
from app import adv
# import app.basic # To call we need to use app.basic.add()
# import app.adv

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



print("Done")
sys.exit(0)