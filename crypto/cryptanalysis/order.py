# Title: Order Calculator of a Generator in Fp
# Creator: Austin Akerley
# Date Created: 12/25/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/20/2020
# Associated Book Page Nuber: N/A
# WARNING: THIS IS A NON-COMPLETE WAY OF FINDING THE ORDER, NEED TO FIX SOMEDAY

# INPUT(s) -
# g - type: int, desc: the element to which you're finding the order of in the field of prime p
# p - type: int, desc: the prime to which you are in the field of

from crypto.cryptanalysis.small_primes_generator import small_primes_generator
from crypto.src.fast_power import fast_power
from crypto.cryptanalysis.naive_factor import naive_factor

def order(g, p, smooth=10000):
    # Naive order method
    if p<1000:
        for i in range(1, p):
            if fast_power(g,i,p) == 1:
                ord = i
                return ord
    h = p-1
    divisors = naive_factor(h).get("divisors")
    # Prime factors and divisors retrieved
    for ord in sorted(divisors): # This should iterate smallest to largest, that way we get teh smallest divisor of e
        result = fast_power(g, ord, p)
        if result == 1: # divisor is the order of g
            return ord

# OUTPUT - type: int
# ord - type: int, desc: The order of element g in the field p
