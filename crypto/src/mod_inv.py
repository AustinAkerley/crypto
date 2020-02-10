# Title: Modular Multiplicative Inverse
# Creator: Austin Akerley
# Date Created: 11/26/2019
# Last Editor: Austin Akerley
# Date Last Edited: 02/09/2020
# Associated Book Page Nuber: 21

# INPUT(S) -
# a - type: int, desc: divisor
# m - type: int, desc: modulus

# Formula: a * inv = 1 (mod m) for all a that does not divide m a.k.a 1/a = inv (mod m_)

# Conditions:
#    1.) a must be smaller than m
#    2.) a and m not equal to 0 or less
#    3.) a cannot divide m

from crypto.src.eea import eea

def mod_inv(a, m): # Where a*b = 1 mod(m)
    inv = None
    if m <= 0: # Error and Base Case Handling
        raise ValueError("m cannot be 0 or less")
    elif a > m:
        raise ValueError("a cannot be larger than m")
    elif a == 0:
        return 0

    else:
        eea_res = eea(a, m)
        inv = eea_res.get("a")
        if eea_res["gcd"] != 1:
            if eea_res["gcd"] != m:
                raise ValueError("a divides m, there is no modular inverse for a:" + str(a)+" with modulo m: "+str(m))
        inv = (inv % m)
    return inv

# OUTPUT - type: int
# inv - type: int, desc: The mathematical inverse modulo m of a, inv = 1/a (mod m), inv*a = 1 (mod m)
