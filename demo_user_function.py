#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO define, name, and call
# a user function (NAMED Block of Code) and optionally pass
# parameters in and optionally return something.
""" 
    DocString
"""
# Example of a user function with optional
# parameter passing. Enforce NAMED parameters using *,
# Default parameters and ANNOTATIONS (Not enforced)
def say_hello(greeting:str="ciao", recipient:str="amici")->None:
    message = f"{greeting} {recipient}"
    print(message)
    return None


say_hello("hello", "my friends") # Positional parameter passing
say_hello(greeting="bonjour", recipient="mes amis") # Named parameter passing
say_hello(recipient="meus amigos", greeting="ol\u00e1") # Named parameters (different order)
say_hello("konichiwa", recipient="tomodachi") # Mixed parameters (positional->named)
say_hello("ciao", 3.14)
say_hello()


print(f"Annotations for say_hello = {say_hello.__annotations__}") # Fact finding