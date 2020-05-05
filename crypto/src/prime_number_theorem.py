# Title: Prime Number Theorem
# Creator: Austin Akerley
# Date Created: 04/04/202
# Last Editor: Austin Akerley
# Date Last Edited: 04/04/2020
# Associated Book Page Nuber: 133

# INPUT(S) -
# limit - type: int, desc: the upper boundary to check the prime number theorem, as it approaches infinity it should get closer to 1

import math
from crypto.src.primality_test import primality_test

def prime_number_theorem(limit):
    number_of_primes = 0
    i_div_ln_i = 0
    ratio = 0
    for i in range(2,limit):
        if i % 10000 == 0:
            ratio = number_of_primes / i_div_ln_i
            print("Ratio : " + str(ratio))
        if primality_test(i, 1000):
            number_of_primes += 1
        i_div_ln_i = i / math.log(i) # When math.log has one arg, it does the natural log, ln
