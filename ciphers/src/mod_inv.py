# Author: Austin Akerley
# Date Last Edited: 10/31/2019
#
from . import eea
def mod_inv(a, m): #Where a*b = 1 mod(m)
    inv = eea.eea(a, m)
    return inv[3] % m
