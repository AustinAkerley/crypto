# Title: Has Square Root
# Creator: Austin Akerley
# Date Created: 12/28/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/19/2020
# Associated Book Page Nuber: N/A

# INPUT(s) -
# a - type: int, desc: the element to check if it has a sqrt in the field {0,1,2...,modulus-1}
# modulus - type: int, desc: the modulus that defines the group of numbers

from crypto.src.fast_power import fast_power

def legendre_symbol(a, modulus):
    ap = fast_power(a, (modulus-1)/2, modulus)
    l_symb = None
    if a==0:
        l_symb = 0
    elif ap == 1: # a is a quadratic residue mod modulus
        l_symb = 1
    elif ap == ((-1) % modulus):# a is a non-quadratic residue mod modulus
        l_symb = -1
    return l_symb

# OUTPUT - type: int
# l_symb - type: int, desc: 0 means it's the modulus, 1 means a has a sqrt in the field of modulus, -1 means it doesn't
