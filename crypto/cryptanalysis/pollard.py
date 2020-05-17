# Title: Pollard's p-1 Factorization Algorithm
# Creator: Austin Akerley
# Date Created: 05/17/2020
# Last Editor: Austin Akerley
# Date Last Edited: 05/17/2020
# Associated Book Page Nuber: 139

# INPUT(s) -
# N - type: int, desc: integer to be factored into p and q, note: p*q = N

from crypto.src.fast_power import fast_power
from crypto.src.eea import eea

def pollard(N):
    a = 2
    p = None
    for j in range(2, 1000):
        a = fast_power(a, j, N)
        d = eea(a-1, N).get("gcd")
        if d > 1 and d < N:
            p = d
            break
    return p

# OUTPUT - type int
# p - type: int, desc: One of the factors of N
