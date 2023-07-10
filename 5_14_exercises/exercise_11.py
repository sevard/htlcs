#!/usr/bin/env python3

from exercise_10 import find_hypot

#####################
# Task for Exerice 11

# Write a function is_rightangled which, given the length of three sides of a triangle,
# will determine whether the triangle is right-angled.
# Assume that the third argument to the function is always the longest side.
# It will return True if the triangle is right-angled, or False otherwise.
#
# Formula to determine whether a triangle is a RIGHT triangle
#      (hypotenuse ** 2) == (a ** 2) + (b ** 2)
#
# Hint: Floating point arithmetic is not always exactly accurate,
# so it is not safe to test floating point numbers for equality.
# If a good programmer wants to know whether x is equal or close enough to y,
# they would probably code it up as:
#   if  abs(x-y) < 0.000001:    # If x is approximately equal to y


#####################
# Task for Exerice 12
# Extend the program so that the sides can be given to the function in any order

def is_rightangled(side_a, side_b, side_c):
    """ Given triangle sides determine whether it is a RIGHT triangle """

    triangle_sides = [side_a, side_b, side_c]
    longest_side = max(triangle_sides)
    triangle_sides.remove(longest_side)

    hypot = find_hypot(*triangle_sides)

    if abs(hypot - longest_side) < 0.000001:
        return True

    return False


result = is_rightangled(10, 15.620499, 12)

print(result)
