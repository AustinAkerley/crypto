# Title: Fast Power Algorithm
# Creator: Austin Akerley
# Date Created: 11/26/2019
# Last Editor: Austin Akerley
# Date Last Edited: 02/09/2020
# Associated Book Page Nuber: 24

# INPUT(s) -
# x - type: int, desc: base of the exponentiation
# e - type: int, desc: exponent
# m - type: int, desc: modulus

# Formula: x^e (mod m) = result

from math import log2

def fast_power(x, e, m): # solvivng x^e (mod m) = result
    # Fermatts little theorem check
    if e == m:
        return x
    elif e == m-1:
        return 1
    elif e == 0:
        return x
    remainder = e
    sum_pwrs_2 = []
    while remainder != 0: # Build e via powers of 2, with the first element being the largest -> 345 ->sum_pwrs_2 = [log2(256), log2(64), ...]
        upper = int(log2(remainder)) # Floor log base 2
        sum_pwrs_2.append(upper)
        remainder = remainder-(2**upper)

    result = 1
    square = x
    for i in range(0, sum_pwrs_2[0]+1):
        if i in sum_pwrs_2:
            result = (result*square) % m
        square = (square*square) % m
    return result

# OUTPUT - type: int
# result - type: int, desc: reuslt = x^e (mod m)
