# Title: Miller-Rabin Primality Test
# Creator: Austin Akerley
# Date Created: 04/04/2020
# Last Editor: Austin Akerley
# Date Last Edited: 04/04/2020
# Associated Book Page Nuber: 131

# INPUT(s) -
# n - type: int, desc: the number you are checking if prime
# certainty - type: int, desc: chance of recieving a false prime charaterisation described by (1/2)^certainty, so the higher certainty the less likely a given number is not actually prime.

import random
from crypto.src.fast_power import fast_power
from crypto.src.eea import eea

def primality_test(n, certainty=50000): #returns true if n is prime, if composite returns false
    if not isinstance(n,int): raise ValueError("n cannot be anything but an int you gave: "+str(type(n)))
    elif n < 1:  raise ValueError("n cannot be less than 0")
    elif n == 1: return True
    elif n%2 == 0: return False
    else:
        for i in range(0, certainty):
            a = random.randint(2, n-1)
            if eea(a, n).get("gcd") != 1: return False
            k = 1
            q = (n-1)/2
            while q%2 == 0:
                k = k + 1
                q = q/2
            a = fast_power(a, q, n)
            if a == 1: continue
            while k > 1:
                if a == -1: break
                a = (a*a)%n
                k = k-1
            if a == -1: continue
        return True

# OUTPUT - type: boolean, desc: True means n is prime, False means n is composite
