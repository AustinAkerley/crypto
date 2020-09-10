# Title: Lenstras Factorization Algorithm
# Creator: Austin Akerley
# Date Created: 12/31/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/20/2020
# Associated Book Page Nuber: 329

# INPUT(s) -
# n - type: int, desc: composite number where n = p*q, where p and q are both primes

import random
from math import sqrt
from math import log2
from crypto.ecc.src.curve import curve
from crypto.src.mod_inv import mod_inv

def lenstras_algorithm(n): # n is a composite number of two large primes, p and q ; n = p*q
    d = n
    i = 0
    while d == n:
        A = random.randint(1,n-1)
        a = random.randint(1,n-1)
        b = random.randint(1, n-1)
        B = ((b*b)%n - (a*a*a)%n - A * a) % n
        E = curve(A, B, n)
        P = (a,b)
        #print("New Curve {"+str(i)+"}")
        for X in range(2, int(log2(n))):
            Q = E.multiply(P, X) # The internals of this will exit() the program and create a divisors of n file in the same directory this was launched
            P = Q
            if len(Q) == 3: # If we've found a divisor of n, could be n itself though
                d = Q[2]
                break
        i+=1
    return d

# OUTPUT - type: int
# d - type: int, desc: a factor of n
