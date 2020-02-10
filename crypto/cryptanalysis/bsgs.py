# Title: Babby Step Giant Step Discrete Logarithm
# Creator: Austin Akerley
# Date Created: 12/25/2019
# Last Editor: Austin Akerley
# Date Last Edited: 02/09/2020
# Associated Book Page Nuber: 82

# INPUTS:
# g - type: int, desc: the small_primes_generator
# h - type: int, desc: the result of the exponentiation
# p - type: int, desc: the prime modulus

# Formula: for any elemnt x in xs: g^x = h (mod p)

from math import log2
from math import sqrt
from crypto.cryptanalysis.order import order
from crypto.src.fast_power import fast_power
from crypto.src.mod_inv import mod_inv

def bsgs(g, h, p, smoothness = 10000): # Solving x given g,h,p for the equation g^x (mod p) = h, so logg(h) (mod p) = x
    N = order(g, p, smoothness)
    n = int(sqrt(N))+1
    e = 1
    u = mod_inv(fast_power(g, n, p), p)
    uk = u
    gi = g
    hui = (h*uk) % p
    list_one = {gi:1}
    list_two = {hui:1}
    # Create the two list
    for i in range(2, n+1):
        gi = (gi*g) % p
        uk = (uk*u) % p
        hui = (h*uk) % p
        list_one.update({gi:i})
        list_two.update({hui:i})
    # Now Check for a collision between the list
    for huk in list_two.keys():
        for gk in list_one.keys():
            if huk == gk:
                x = (list_one.get(gk) + (list_two.get(huk) * n)) % N
                xs = []
                for i in range(0, int(((p-1)/N)+1)):
                    xs.append(x+N*i)
                return xs
# OUTPUTS:
# xs- type: list of ints, desc: every x in xs is equivalent to x = log(h) (mod p)
