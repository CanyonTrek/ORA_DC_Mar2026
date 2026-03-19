#! /usr/bin/env python3
# Author: DCameron
# Description: This module defines a class of Tank
""" 
    Tank Class for an online Tank game
"""

class Tank:
    # A class has TWO components = attributes/Data + Behaviour/Methods
    def __init__(self, country, model):
        self.country = country
        self.model = model
        self._speed = 0
        self._health = 100
        self._direction = 0
        self._location = {'x':0, 'y':0, 'z':0}
        self._shells = 20
        # No explicit return as called IMPLICITLY!

    def accel(self, increase):
        self._speed += increase
        return None

    def decel(self, decrease):
        self._speed -= decrease
        return None

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
