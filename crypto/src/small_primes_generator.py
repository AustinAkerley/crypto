# Author: Austin Akerley
# Date Last Edited: 11/27/2019
#
# INPUTS:
# max : int  -  The value to find all prime integers under
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

# OUTPUTS:
# small_primes : list of integers - complete list of primes integers < max
