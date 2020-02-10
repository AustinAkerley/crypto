# Title: Square Root Calculator in Modulo Arithmetic
# Creator: Austin Akerley
# Date Created: 12/28/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/18/2019
# Associated Book Page Nuber: 169

# INPUT(s) -
# a - type: int, desc: the number ur computing the sqrt of in the group {0,1,2...,modulus-1}
# modulus - type: int, desc: the modulus that defines the group of numbers

# Formula: (root1, root2) = sqrt(a) (mod modulus)

import random
from crypto.src.fast_power import fast_power
from crypto.src.legendre_symbol import legendre_symbol

def mod_sqrt(a, modulus):
    root1 = None
    root2 = None
    if legendre_symbol(a, modulus) != 1:
        root1 = None
        root2 = None
    elif modulus % 2 == 0: # Non-prime modulus's are not supported
        print("Not a prime")
        root1 = None
        root2 = None
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
        while legendre_symbol(z, modulus) != -1: # z is a non-quadratic residue
            z = random.randint(1,modulus-1)
        c = fast_power(z, m, modulus)
        x = fast_power(a, (m+1)/2, modulus)
        t = fast_power(a, m, modulus)
        while t != 1:
            i = 1
            for i in range(1, e):
                if fast_power(t, 2**i, modulus) == 1:
                    break
            b = fast_power(c, 2**(e-i-1), modulus)
            x = (b*x) % modulus
            t = (t*b*b) % modulus
            c = (b*b) % modulus
            e = i
        root1 = x
        root2 = modulus-x
    elif modulus % 8 == 3 or modulus % 8 == 7:
        x = fast_power(a, (modulus + 1) / 4, modulus)
        root1 = x
        root2 = (-x)%modulus
    return (root1, root2)

# OUTPUT - type: tuple
# (
#   root1 - type: int, desc: One of the two roots of | sqrt(a) (mod modulus) |
#   root2 - type: int, desc: One of the two roots of | sqrt(a) (mod modulus) |
# )
