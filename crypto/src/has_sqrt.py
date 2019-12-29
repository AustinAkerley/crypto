# Title: Has Square Root
# Creator: Austin Akerley
# Date Created: 12/28/2019
# Last Editor: Austin Akerley
# Date Last Edited: 12/28/2019
# Associated Book Page Nuber: XXXXXXXX

from crypto.src.fast_power import fast_power

def has_sqrt(a, modulus):
    a_if_has_sqrt = fast_power(a, (modulus+1)/2, modulus).get("result")
    if a == a_if_has_sqrt:
        return True
    return False
