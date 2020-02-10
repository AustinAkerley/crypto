# Title: Chinese Remainder Theorem
# Creator: Austin Akerley
# Date Created: 11/26/2019
# Last Editor: Austin Akerley
# Date Last Edited: 02/09/2020
# Associated Book Page Nuber: 84

# INPUT(s) -
# congruences_and_primes - type: list of tuples, desc: a list of tuples of any size that is a congruence and the prime associated like this [(a0, p0), (a1, p1), ... , (an, pn)], exmaple: [(8, 13),(2, 11)]

from crypto.src.mod_inv import mod_inv

def crt(congruences_and_primes): # return x where x = ax (mod m), where m is p0*p1*...*pn
    i = 0
    x = 0
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
            inv_p_last = mod_inv((p_last%px), px)
            y = (((ax-a_last)%px) * inv_p_last) % px
            x = (a_last + (y*p_last)) % (p_last*px)
            a_last = x
            p_last = (p_last*px)
    return x

# OUTPUT - type int
# x - type: int, desc: retun value is x where x = a0 (mod p0), x = a1 (mod p1), x = a2 (mod p2)... With all of the ai's and pi's, you can solve backwards for x by the method above, example: 83
