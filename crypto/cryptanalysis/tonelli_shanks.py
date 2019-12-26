# Author: Austin Akerley
# Date Last Edited: 11/22/2019
#

# TODO: MULTI PROCESS, FILES INSTEAD OF MEMORY, MAKE ORDER BETTER

# INPUTS:
# g : int - the small_primes_generator
# h : int - the result of the exponentiation
# p : int - the prime modulus

from math import log2
from math import sqrt
from crypto.cryptanalysis.order import order
from crypto.src.fast_power import fast_power
from crypto.src.mod_inv import mod_inv

def tonelli_shanks(g, h, p): #Solving x given g,h,p for the equation g^x (mod p) = h, so logg(h) (mod p) = x
    smoothness = 1000
    N = order(g, p, smoothness)["order"]  # Need a more complete way to solve for the order of N
    n = int(sqrt(N))+1
    gn = fast_power(g, n, p)["result"]
    u = mod_inv(gn, p)
    uk = u
    gi = g
    hi = (h*u) % p
    list_one = {gi:1}
    list_two = {hi:1}
    i=2
    # Create the two list
    while i<=n:
        gi = (gi*g) % p
        uk = (uk*u) % p
        hi = (h*uk) % p
        list_one.update({gi:i})
        list_two.update({hi:i})
        i+=1
    # Check for a collision between the list
    for huk in list_two.keys():
        for gk in list_one.keys():
            if huk == gk:
                x = list_one.get(gk) + (list_two.get(huk) * n)
                return x
# OUTPUTS:
# x : int - x where x = logg(h) (mod p)
