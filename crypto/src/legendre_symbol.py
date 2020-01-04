# Title: Has Square Root
# Creator: Austin Akerley
# Date Created: 12/28/2019
# Last Editor: Austin Akerley
# Date Last Edited: 12/28/2019
# Associated Book Page Nuber: XXXXXXXX

from crypto.src.fast_power import fast_power

def legendre_symbol(a, modulus):
    ap = fast_power(a, (modulus-1)/2, modulus).get("result")
    if a==0:
        return 0
    elif ap == 1:
        return 1
    elif ap == ((-1) % modulus):
        return -1
    else:
        return None
