#!/usr/bin/env python3

# Write a function which is given an exam mark, 
# and it returns a string — the grade for that mark — according to this scheme:

#    Mark      Grade
# ----------|--------------
#  >= 75    | First
# [70-75)   | Upper Second 
# [60-70)   | Second
# [50-60)   | Third
# [45-50)   | F1 Supp
# [40-45)   | F2
#  < 40     | F3

# The square and round brackets denote closed and open intervals. 
# A closed interval includes the number, 
# and open interval excludes it. 
# So 39.99999 gets grade F3, but 40 gets grade F2. Assume

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
                     49.9, 45, 44.9, 40, 39.9, 2, 0]


def get_grade(mark):
    
    if mark >= 75:
        grade = "First"
    elif mark >= 70 and mark < 75:
        grade = "Upper Second"
    elif mark >= 60 and mark < 70:
        grade = "Second"
    elif mark >= 50 and mark < 60:
        grade = "Third"
    elif mark >= 45 and mark < 50:
        grade = "F1 Supp"
    elif mark >= 40 and mark < 45:
        grade = "F2"
    elif mark < 40:
        grade = "F3" 

    return grade

for score in xs:
    print(score, get_grade(score))

assert get_grade(83) == "First"
assert get_grade(75) == "First"
assert get_grade(74.9) == "Upper Second"
assert get_grade(70) == "Upper Second"
assert get_grade(69.9) == "Second"
assert get_grade(65) == "Second"
assert get_grade(60) == "Second"
assert get_grade(59.9) == "Third"
assert get_grade(55) == "Third"
assert get_grade(50) == "Third"
assert get_grade(49.9) == "F1 Supp"
assert get_grade(44.9) == "F2"
assert get_grade(40) == "F2"
assert get_grade(39) == "F3"
assert get_grade(2) == "F3"
assert get_grade(0) == "F3"
