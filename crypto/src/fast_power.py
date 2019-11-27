# Author: Austin Akerley
# Date Last Edited: 10/31/2019
#
from math import log2
def fast_power(x, e, m, known_powers=None): #solivng for x^e (mod m) = result, where known_powers is a dictionary of powers and there result for the same x and m
    #Fermatts little theorem addition
    # TODO: Add a check to see if m is prime.
    if e == m:
        return [0, {}]
    elif e == m-1:
        return [1, {}]

    remainder = e
    sum_pwrs_2 = []
    while remainder != 0: #Build e via powers of 2, with the first elemnet being the largest -> 345 ->sum_pwrs_2 = [256, 64, ...]
        upper = int(log2(remainder)) # floor log base 2
        sum_pwrs_2.append(upper)
        remainder = remainder-(2**upper)

    #The idea behind known powers is to not recompute powers that are already known this will benefit things such as iterating through x^e mod m where e={0,1,2,...n} for any large number n
    if known_powers is not None: # known_powers is of the  structure where (x^(2^i)) and  {{i:ci},{i+1,ci+1},...}
        result = 1
        for i in range(0, sum_pwrs_2[0]+1):
            if i not in known_powers.keys(): #added needed values to known powers
                if i == 0:
                    known_powers.update({0:x})
                else:
                    j=i-1
                    while j not in known_powers.keys():#Figure out how far back I need to go
                        j-=1
                    while j<i: #Update known_powers
                        square = known_powers.get(j)
                        square = (square*square) % m
                        known_powers.update({j+1:square})
            #Values needed are already in known known_powers
            result = (result*known_powers.get(i)) % m
        return [result, known_powers]

    else:
        known_powers = {}
        result = 1
        square = x
        for i in range(0, sum_pwrs_2[0]+1):
            if i in sum_pwrs_2:
                result = (result*square) % m
            known_powers.update({i:square})
            square = (square*square) % m

        return [result, known_powers]
