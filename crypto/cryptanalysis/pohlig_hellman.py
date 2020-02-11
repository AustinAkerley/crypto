# Title: Pohlig Hellman Discrete Logarith
# Creator: Austin Akerley
# Date Created: 01/27/2020
# Last Editor: Austin Akerley
# Date Last Edited: 01/27/2020
# Associated Book Page Nuber: 87

# INPUTS:
# g - type: int, desc: the small_primes_generator
# h - type: int, desc: the result of the exponentiation
# p - type: int, desc: the prime modulus

from crypto.cryptanalysis.crt import crt
from crypto.cryptanalysis.naive_factor import naive_factor
from crypto.cryptanalysis.bsgs import bsgs
from crypto.cryptanalysis.order import order
from crypto.src.fast_power import fast_power

def pohlig_hellman(g, h, p): #Solving x given g,h,p for the equation g^x (mod p) = h, so logg(h) (mod p) = x
    n = p-1
    congruences_and_mods = []
    prime_factors = naive_factor(n, 10000).get("prime_factors_dict")
    for factor in prime_factors.keys():
        modulo = factor ** prime_factors.get(factor)
        gi = fast_power(g, n/modulo, p)
        hi = fast_power(h, n/modulo, p)
        ax = bsgs(gi, hi, p)[0] # retuns a list of solutions, we just want the first one
        congruences_and_mods.append((ax, modulo))
    x = crt(congruences_and_mods)
    N = order(g, p, 10000)
    xs = []
    for i in range(1, int(((p-1)/N)+1)):
        xs.append(int((x+N*i)%n))
    return xs

# OUTPUTS:
# x - type: int, desc: x where x = log(h) (mod p)
