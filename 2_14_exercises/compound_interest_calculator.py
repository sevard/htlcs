#!/usr/bin/env python3


# Formula a = P(1 + r/n)nt

# P => principal amount
# r => annual nominal interest rate (as a decimal)
# n => number of times the interest is calculated per year
# t => number of years
# Calculate and print the amount after 't' years

def calculate_compound_interest(years):
    """ Calculate total compound interest """

    p = 10000
    n = 12
    r = 0.08

    return p * (1 + r/n) ** (n * years)

print(calculate_compound_interest(2))
print(calculate_compound_interest(5))
