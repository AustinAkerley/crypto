# Title: Naive Factoring Algorithm
# Creator: Austin Akerley
# Date Created: 12/25/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/20/2020
# Associated Book Page Nuber: N/A

# INPUT(s) -
# h - type: int, desc: number to try to factor
# smooth - type: int, desc: tells the program the upper limit to check if divisble by

from crypto.src.small_primes_generator import small_primes_generator

def naive_factor(h, smooth=1000):
    prime_factors = []
    small_primes = small_primes_generator(smooth)
    divisors = []
    #  Naive stratedgy for computing order
    # Compile a list of factors up to a certain smoothness then attempt to find the smallest solution to g^c % p = 1 , where c is any combination of the factors of g
    for prime in small_primes:
        while h % prime == 0:
            h = h/prime
            prime_factors.append(prime)
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
        prime_factors.append(h)
        new_divisors = []
        for divisor in divisors:
            new_divisor = divisor * h
            new_divisors.append(new_divisor)
        divisors.append(h)
        for nd in new_divisors:
            if nd not in divisors:
                divisors.append(nd)
    return {"divisors":divisors, "prime_factors": prime_factors}

# OUTPUT - type: dictionary
# {
#    "divisors" : divisors -  list of int - a list of unique divisors of h, h%divisors = 0 for all divisors
#    "prime_factors" : prime factors -  list of int - a list of all of the numbers to make up h, h = prime_factors[0]*prime_factors[1]*...*prime_factors[n]
# }
