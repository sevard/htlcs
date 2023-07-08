

l = [1, 3]

def find_hypot(*sides):
    print(sides)
    """ Calculate hypotenuse length based on side lengths """
    side_a = sides[0]
    side_b = sides[1]
    sum_of_sides = (side_a ** 2) + (side_b ** 2)
    hypot = sum_of_sides ** 0.5 # calculate the sqrt 
    return hypot

h = find_hypot(l)
print(h)