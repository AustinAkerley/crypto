# Author: Austin Akerley
# Date Last Edited: 11/27/2019
#
from crypto.src.small_primes_generator import small_primes_generator
from crypto.src.fast_power import fast_power

def order(g, e, p, smooth=1000):
    print("order1")
    prime_factorization = []
    small_primes = small_primes_generator(smooth)
    print("order2")
    divisors = []
    #  Naive stratedgy for computing order
    # Compile a list of factors up to a certain smoothness then attempt to find the smallest solution to g^c % p = 1 , where c is any combination of the factors of g
    h = e #create copy so we can mantain g's orginal valuye
    print("order3")
    for prime in small_primes:
        while h % prime == 0:
            h = h/prime
            prime_factorization.append(prime)
            for divisor in divisors:
                new_divisor = divisor * prime
                divisors.append(new_divisor)
            if prime not in divisors:
                divisors.append(prime)
    print("order4")

    prime_factorization.append(h)
    for divisor in divisors:
        new_divisor = divisor * h
        divisors.append(new_divisor)
    divisors.append(h)
    print("order5")
    # Prime factors retrieved
    known_powers = {}
    print("length of divisors: "+str(len(divisors)))
    for divisor in sorted(divisors): # This should iterate smallest to largest, that way we get teh smallest divisor of e
        result = fast_power(g, divisor, p, known_powers)
        known_powers = result[1]
        if result[0] == 1: # result[0] is the order of g
            order = result[0]
            return order #
    print("order6")
