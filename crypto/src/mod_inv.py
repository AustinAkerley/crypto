# Title: Modular Multiplicative Inverse
# Creator: Austin Akerley
# Date Created: 11/26/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/19/2020
# Associated Book Page Nuber: 21
# NOTE: NOT HAPPY WITH HOW THIS WAS DONE! NEED TO FIX SOON, SHOULD NOT HAVE A DICT RETUN, SEE ECC LENTRAS FASCT TO FIX

# INPUT(S) -
# a - type: int, desc: divisor
# m - type: int, desc: modulus

from crypto.src.eea import eea

def mod_inv(a, m): # Where a*b = 1 mod(m)
    eea_res = eea(a, m)
    inv = eea_res.get("a")
    if eea_res["gcd"] != 1:
        if eea_res["gcd"] != m:
            print(str(eea_res["gcd"]) + " divides N = {"+str(m)+"}" )
        return (None, eea_res["gcd"])
    inv = (inv % m)
    return inv

# OUTPUT - type: int
# inv - type: int, desc: The mathematical inverse modulo m of a, inv = 1/a (mod m), inv*a = 1 (mod m)
