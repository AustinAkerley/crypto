# Author: Austin Akerley
# Date Last Edited: 11/27/2019
#
from crypto.src.small_primes_generator import small_primes_generator
from crypto.src.fast_power import fast_power

def order(g, e, p, smooth=1000):
    prime_factorization = []
    small_primes = small_primes_generator(smooth)
    divisors = []
    #  Naive stratedgy for computing order
    # Compile a list of factors up to a certain smoothness then attempt to find the smallest solution to g^c % p = 1 , where c is any combination of the factors of g
    h = e #create copy so we can mantain g's orginal valuye
    for prime in small_primes:
        while h % prime == 0:
            h = h/prime
            prime_factorization.append(prime)
            new_divisors = []
            for divisor in divisors:
                new_divisor = divisor * prime
                new_divisors.append(new_divisor)
            for nd in new_divisors:
                if nd not in divisors:
                    divisors.append(nd)
            if prime not in divisors:
                divisors.append(prime)
    h = int(h)
    if h!=1:
        prime_factorization.append(h)
        new_divisors = []
        for divisor in divisors:
            new_divisor = divisor * h
            new_divisors.append(new_divisor)
        divisors.append(h)
        for nd in new_divisors:
            if nd not in divisors:
                divisors.append(nd)
    # Prime factors and divisors retrieved
    known_powers = {}
    for divisor in sorted(divisors): # This should iterate smallest to largest, that way we get teh smallest divisor of e
        result = fast_power(g, divisor, p, known_powers)
        known_powers = result[1]
        if result[0] == 1: # divisor is the order of g
            order = divisor
            print("order: "+str(order))
            return order
