# Author: Austin Akerley
# Date Last Edited: 10/31/2019
#
# INPUTS:
# a : int         - divisor
# m : int         - modulus

from crypto.src.eea import eea
def mod_inv(a, m): #Where a*b = 1 mod(m)
    inv = eea(a, m)["a"]
    return (inv % m)

# OUTPUTS: int
# inv  -  The mathematical inverse modulo m of a, inv = 1/a (mod m), inv*a = 1 (mod m)
