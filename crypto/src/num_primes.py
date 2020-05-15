# Title: Approximate Number of Primes In A Given Range
# Creator: Austin Akerley
# Date Created: 04/04/2020
# Last Editor: Austin Akerley
# Date Last Edited: 04/04/2020
# Associated Book Page Nuber: 133

# INPUT(S) -
# x - type: int, desc: lower nuumber of the range
# y - type: int, desc: higher number of the range

# Returns the approximate number of primes between x and y and prints the percentage of prime numbers in that range

import math

def num_primes(x=1, y=1000000):
    if y < x: raise ValueError("y must be bigger than x")
    approx = (y/math.log(y)) - (x/math.log(x))
    percentage = 100 * (approx / (y-x))
    print("The percentage of primes between "+str(x) + " and "+str(y) + " is %" + str(percentage))
    return int(approx + 0.5)
