# Author: Austin Akerley
# Date Last Edited: 11/24/2019
# Title: Chinese Remainder Theorem
from crypto.src.mod_inv import mod_inv
def crt(congruences_and_primes): # congruences_and_primes is of the form: [(a0, p0), (a1, p1), ... , (an, pn)] where an, pn must be a tuple, solving for x where x = ax (mod px) for all x in range 0-n
    i=0
    x=0
    a_last = 0
    p_last = 0
    for ax_px in congruences_and_primes:
        if i == 0:
            a_last = ax_px[0]
            p_last = ax_px[1]
            i+=1
        else:
            ax = ax_px[0]
            px = ax_px[1]
            # ax-a_last = p_last * y (mod px)
            #print( str(ax) + " - " + str(a_last) + " = " + str(p_last) + " * y (mod " + str(px) + ")")
            inv_p_last = mod_inv((p_last%px), px)
            y = (((ax-a_last)%px) * inv_p_last) % px
            x = (a_last + (y*p_last)) % (p_last*px)
            a_last = x
            p_last = (p_last*px)
    return x
