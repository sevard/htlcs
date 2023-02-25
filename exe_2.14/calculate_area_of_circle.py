#!/usr/bin/env python3

# Calcualte the area of a circle
# Area = pi * r ** 2


def find_circle_area(radius):
    """ Calculate the area of a circle """
    if radius == 0:
        return None

    if not isinstance(radius, (int, float, str)):
        return None

    if isinstance(radius, str) and not radius.isdigit():
        return None

    if isinstance(radius, str) and radius.isdigit():
        radius = float(radius)

    PI = 3.141592653589793
    area = PI * (radius ** 2)
    return area

if __name__ == '__main__':

    assert find_circle_area(0) == None
    assert find_circle_area([]) == None
    assert find_circle_area({'a': 1}) == None
    assert find_circle_area({}) == None
    assert find_circle_area('') == None
    assert find_circle_area('abc') == None
    assert find_circle_area(123) == 47529.15525615998

