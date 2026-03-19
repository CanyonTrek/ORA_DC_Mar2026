#! /usr/bin/env python3
# Author: DCameron
# Description: This module defines a class of Tank
""" 
    Tank Class for an online Tank game
"""
from app import vehicle

class Tank(vehicle.Vehicle):
    # A class has TWO components = attributes/Data + Behaviour/Methods
    def __init__(self, country, model):
        vehicle.Vehicle.__init__(self, country, model)
        self._health = 100
        self._direction = 0
        self._location = {'x':0, 'y':0, 'z':0}
        self._shells = 20
        # No explicit return as called IMPLICITLY!

    def rotate_left(self, degrees):
        self._direction -= degrees % 360
        return None

    def rotate_right(self, degrees):
        self._direction += degrees % 360
        return None

    def shoot(self):
        self._shells -= 1
        return None

    def take_damage(self, damage):
        self._health -= damage
        return None

    # And now for some SPECIAL methods..
    # Example of Operator Overloading
    def __add__(self, other):
        return self._health + other._health

    # Examples of GETTER and SETTERs
    def get_health(self):
        return self._health

    def set_health(self, new_health):
        self._health = new_health
        return None

    # Wrap one variable name interface to the getter+setter
    # tank_health = property(get_health, set_health)

    # ALTERNATIVELY we could use DECORATORS
    @property
    def tank_health(self):
        return self._health

    @tank_health.setter
    def tank_health(self, new_health):
        self._health = new_health
        return None

    def __del__(self):
        print("Boom..boom..boom")
        return None