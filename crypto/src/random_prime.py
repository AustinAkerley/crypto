# WARNING: This is not a secure method, it is solely for testing purposes
# Title: Random Prime Generator
# Creator: Austin Akerley
# Date Created: 08/07/2020
# Last Editor: Austin Akerley
# Date Last Edited: 08/07/2020
# Associated Book Page Nuber:

# INPUT(s) -
# bits - type: int, desc: number of max bits you want your random prime number to be

import random
from crypto.src.primality_test import primality_test

def random_prime(bits):
    max_int = ""
    for i in range(0,bits):
        max_int += "1"
    max = int(max_int, 2)
    rand = random.randint(1,max)
    if rand % 2 == 0:
        rand+=1
    while not primality_test(rand):
        rand = (rand + 2) % max
    return rand
