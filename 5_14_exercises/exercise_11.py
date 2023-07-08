#!/usr/bin/env python3

from exercise_10 import find_hypot


# Write a function is_rightangled which, given the length of three sides of a triangle,
# will determine whether the triangle is right-angled.
# Assume that the third argument to the function is always the longest side.
# It will return True if the triangle is right-angled, or False otherwise.

# Formula to determine whether a triangle is a RIGHT triangle is: (hypotenuse ** 2) == (a ** 2) + (b ** 2)

# Hint: Floating point arithmetic is not always exactly accurate,
# so it is not safe to test floating point numbers for equality.
# If a good programmer wants to know whether x is equal or close enough to y,
# they would probably code it up as:
#   if  abs(x-y) < 0.000001:    # If x is approximately equal to y

def is_rightangled(a, b, c, debug=False):
    """ Given triangle sides 'a' 'b' 'c' determine whether it is a RIGHT triangle 
        Assume that the third argument to the function is always the longest side.
    """
    h = find_hypot(a, b)

    if abs(h - c) < 0.000001:
        if debug:
            print(f"abs(h - c): {abs(h - c)}")
            print(F"{h} == {c} (h is approximately equal to c)")
        return True

    if debug:
        print(F"{h} (h) != {c} (c)")

    return False


result = is_rightangled(10, 12, 15.620499, True)

print(result)
