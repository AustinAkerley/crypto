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

from crypto.src.small_primes_generator import small_primes_generator
from crypto.src.fast_power import fast_power
from crypto.cryptanalysis.naive_factor import naive_factor

def order(g, p, smooth=1000):
    h = p-1
    div_and_factors = naive_factor(h)
    divisors = div_and_factors["divisors"]
    prime_factors = div_and_factors["prime_factors"]
    # Prime factors and divisors retrieved
    known_powers = {}
    for divisor in sorted(divisors): # This should iterate smallest to largest, that way we get teh smallest divisor of e
        result = fast_power(g, divisor, p, known_powers)
        known_powers = result["known_powers"]
        if result["result"] == 1: # divisor is the order of g
            order = divisor
            print("order: "+str(order))
            return {"order":order, "divisors":divisors, "prime_factors":prime_factors}

# OUTPUT - type: dictionary
# {
#     "order" : order, - The true result of the function, tells you the order of g in field Fp
#     "divisors" : divisors, - All of the divisors of p-1
#     "prime_factors":prime_factors - All of the prime factors of p-1
# }
