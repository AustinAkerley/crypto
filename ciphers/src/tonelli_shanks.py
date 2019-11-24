# Author: Austin Akerley
# Date Last Edited: 11/22/2019
#
from .ciphers.src.fast_power import fast_power
def tonelli_shanks(g, h, p): #Solving x given g,h,p for the equation g^x (mod p) = h, so logg(h) (mod p) = x
