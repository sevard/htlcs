#!/usr/bin/env python3


# Task: Write a function find_hypot which, given the length of two sides of a right-angled triangle,
# returns the length of the hypotenuse. (Hint: x ** 0.5 will return the square root.)

# Formula to find the hypotenuse is sqrt( (a ** 2) + (b ** 2) )

def find_hypot(side_a, side_b):
    """ Calculate hypotenuse length based on side lengths """

    sum_of_sides = (side_a ** 2) + (side_b ** 2)
    hypot = sum_of_sides ** 0.5 # calculate the sqrt 
    return hypot


assert find_hypot(10, 12) == 15.620499351813308
assert find_hypot(0.7087, 0.5504) == 0.8973270585466595
assert find_hypot(0.1, 0.1) == 0.14142135623730953
