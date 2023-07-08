#!/usr/bin/env python3


# Task: Write a function find_hypot which, given the length of two sides of a right-angled triangle,
# returns the length of the hypotenuse. (Hint: x ** 0.5 will return the square root.)

# Formula to find the hypotenuse is sqrt( (a ** 2) + (b ** 2) )

def find_hypot(side_a, side_b):
    """ Calculate hypotenuse based on side lengths """

    sides = (side_a ** 2) + (side_b ** 2)
    hypot = sides ** 0.5
    return hypot


if __name__ == '__main__':

    print(find_hypot(10, 12))
