# Give the logical opposites of these conditions
# a = 1
# b = 2
# day = a + b

# a > b
# a >= b
# a >= 18  and  day == 3
# a >= 18  and  day != 3

# # logical opposites
# a <= b
# a < b
# a < 18 or day != 3
# a < 18 or day == 3

# ------ Exercise 4 -------- #
# What do these expressions evaluate to?
# print(3 == 3) # True 
# print(3 != 3) # False
# print(3 >= 4) # False
# print(not (3 < 4)) # Fasle

# ------ Exercise 5 -------- #
# Evaluate this truch table
#  p  q  r   (not (p and q)) or r
#  F  F  F    T
print((not (False and False) ) or False) # True

#  F  F  T    T
print((not (False and False) ) or True) # True

#  F  T  F    T
print((not (False and True) ) or False) # True

#  F  T  T    T
print((not (False and True) ) or True) # True

#  T  F  F    T
print((not (True and False) ) or False) # True

#  T  T  F    F
print((not (True and True) ) or False) # False 

#  T  T  T    T
print((not (True and True) ) or True) # True 