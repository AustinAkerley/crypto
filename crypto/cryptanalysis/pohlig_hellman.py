# Title: Pohlig Hellman Discrete Logarith
# Creator: Austin Akerley
# Date Created: 01/27/2020
# Last Editor: Austin Akerley
# Date Last Edited: 01/27/2020
# Associated Book Page Nuber: 87
# TODO: MULTI PROCESS, FILES INSTEAD OF MEMORY, MAKE ORDER BETTER

# INPUTS:
# g - type: int, desc: the small_primes_generator
# h - type: int, desc: the result of the exponentiation
# p - type: int, desc: the prime modulus

#from math import log2
#from math import sqrt
#from crypto.cryptanalysis.order import order
from crypto.src.crt import crt
from crypto.cryptanalysis.naive_factor import naive_factor
from crypto.cryptanalysis.tonelli_shanks import tonelli_shanks
from crypto.src.fast_power import fast_power

def pohlig_hellman(g, h, p): #Solving x given g,h,p for the equation g^x (mod p) = h, so logg(h) (mod p) = x
    n = p-1
    congruences_and_mods = []
    prime_factors = naive_factor(n, 10000).get("prime_factors_dict")
    for factor in prime_factors.keys():
        modulo = factor ** prime_factors.get(factor)
        gi = fast_power(g, n/modulo, factor).get("result")
        hi = fast_power(h, n/modulo, factor).get("result")
        print("gi: "+str(gi)+ " | hi: "+str(hi)+" | factor: "+str(factor))
        x = tonelli_shanks(gi, hi, factor)

        congruences_and_mods.append((x, factor))
    print(congruences_and_mods)
    return crt(congruences_and_mods)






# OUTPUTS:
# x - type: int, desc: x where x = log(h) (mod p)
