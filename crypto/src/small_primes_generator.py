# Title: Small Primes Generator
# Creator: Austin Akerley
# Date Created: 11/26/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/18/2019
# Associated Book Page Nuber: N/A

# INPUT(s) -
# max - type: int, desc: The value to find all prime integers under

def small_primes_generator(max): #max being
    small_primes = [2,3,5]
    for i in range (7,max):
        is_prime = True
        for prime in small_primes:
            if i%prime == 0:
                is_prime = False
        if is_prime:
            small_primes.append(i)
    return small_primes

# OUTPUT - type: list
# small_primes - type: list of integers, desc: complete list of primes integers les than max
