# Title: Modular Multiplicative Inverse
# Creator: Austin Akerley
# Date Created: 11/26/2019
# Last Editor: Austin Akerley
# Date Last Edited:12/28/2019
# Associated Book Page Nuber: XXXXXXXX

# INPUTS:
# a : int         - divisor
# m : int         - modulus

from crypto.src.eea import eea

def mod_inv(a, m): #Where a*b = 1 mod(m)
    inv = eea(a, m)["a"]
    return (inv % m)

# OUTPUTS: int
# inv  -  The mathematical inverse modulo m of a, inv = 1/a (mod m), inv*a = 1 (mod m)
