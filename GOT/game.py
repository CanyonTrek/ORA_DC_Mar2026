#! /usr/bin/env python3
# Author: DCameron
# Description: This is an ultra realistic online game with Tanks
""" 
    GOT - Game of Tanks
"""
import sys
from app import tank

def main():
    # Create/Instantiate 3 Tank Objects
    joe_tank = tank.Tank('german', 'tiger')
    bri_tank = tank.Tank('american', 'sherman')
    celso_tank = tank.Tank('british', 'churchill')

    # And the game begins..
    joe_tank.accel(63)
    bri_tank.accel(29)

    celso_tank.rotate_left(289)
    celso_tank.accel(32)
    celso_tank.shoot()

    # And success..
    joe_tank.take_damage(54)
    bri_tank.take_damage(32)

    # And now for some visuals..
    print(f"Health of Joe's Tank is {joe_tank._health}") # POOR CODE

    # Example of Operator Overloading
    print(f"Health of Joe's and Bri's Tanks are {joe_tank + bri_tank}")

    # Joe receives a HEALTH Boost
    # joe_tank._health = 100
    # print(f"New health of Joe's Tank = {joe_tank._health}")
    joe_tank.set_health(101) # GOOD = SETTER method
    print(f"New health of Joe's Tank = {joe_tank.get_health()}") # GOOD = GETTER method
    joe_tank.tank_health = 102
    print(f"New health of Joe's Tank = {joe_tank.tank_health}")  # GOOD = GETTER method
    return None


if __name__ == "__main__":
    # Execute only if ran directly as a program
    # ignored if imported as a module.
    main()
    sys.exit(0)