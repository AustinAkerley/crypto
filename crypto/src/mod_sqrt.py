# Title: Square Root Calculator in Modulo Arithmetic
# Creator: Austin Akerley
# Date Created: 12/28/2019
# Last Editor: Austin Akerley
# Date Last Edited: 12/28/2019
# Associated Book Page Nuber: XXXXXXXX

import random
from crypto.src.fast_power import fast_power
from crypto.src.legendre_symbol import legendre_symbol

def mod_sqrt(a, modulus):
    if legendre_symbol(a, modulus) != 1:
        print("a {"+str(a)+"} has no square root modulo {"+str(modulus)+"}")
        return None
    if modulus % 2 == 0:
        print("Not a prime")
        return None
    elif modulus % 8 == 1 or modulus % 8 == 5:
        s = 0
        m = None
        n = modulus-1
        while n%2==0:
            n = n/2
            s+=1
        m = n
        e = s
        z = random.randint(1,modulus-1)
        while legendre_symbol(z, modulus) != -1:
            z = random.randint(1,modulus-1)
        # z is a quadratic non-residue
        c = fast_power(z, m, modulus).get("result")
        x = fast_power(a, (m+1)/2, modulus).get("result")
        t = fast_power(a, m, modulus).get("result")
        while t != 1:
            i = 1
            for i in range(1, e):
                if fast_power(t, 2**i, modulus).get("result") == 1:
                    break
            b = fast_power(c, 2**(e-i-1), modulus).get("result")
            x = (b*x) % modulus
            t = (t*b*b) % modulus
            c = (b*b) % modulus
            e = i
        return (x, modulus-x)
        print("1");
    elif modulus % 8 == 3 or modulus % 8 == 7:
        x = fast_power(a, (modulus + 1) / 4, modulus).get("result")
        return (x, (-x)%modulus)
    else: # you. are. bad.
        return None;
