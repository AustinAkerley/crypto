# Title: Square Root Calculator in Modulo Arithmetic
# Creator: Austin Akerley
# Date Created: 12/28/2019
# Last Editor: Austin Akerley
# Date Last Edited: 12/28/2019
# Associated Book Page Nuber: XXXXXXXX

from crypto.src.fast_power import fast_power

def mod_sqrt(a, modulus):
    if modulus % 2 == 0:
        print("Not a prime")
        return None
    elif modulus % 8 == 1:
        print("1");
    elif modulus % 8 == 3 or modulus % 8 == 7:
        x = fast_power(a, (modulus + 1) / 4, modulus).get("result")
        return (x, (-x)%modulus)
    elif modulus % 8 == 5:
        print("5");
    else: # bad
        return None;
