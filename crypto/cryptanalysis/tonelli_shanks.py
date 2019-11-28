# Author: Austin Akerley
# Date Last Edited: 11/22/2019
#
from math import log2
from math import sqrt
from crypto.src.order import order
from crypto.src.fast_power import fast_power
from crypto.src.mod_inv import mod_inv

def tonelli_shanks(g, h, p, check_interval = 2): #Solving x given g,h,p for the equation g^x (mod p) = h, so logg(h) (mod p) = x
    smoothness = 1000
    N = order(g,p-1, p, smoothness)
    n = int(sqrt(N))+1 # Need a better way to solve for the order of N
    gn = fast_power(g, n, p)[0]
    #print("gn: "+str(gn))
    u = mod_inv(gn, p)
    #print("u: "+str(u))

    uk = u
    gi = g
    hi = (h*u) % p
    list_one = {gi:1}
    list_two = {hi:1}
    i=2

    for intv in range(1,check_interval+1):
        while i<=n*intv/check_interval:
            gi = (gi*g) % p
            uk = (uk*u) % p
            hi = (h*uk) % p
            #print("gi: "+str(gi))
            #print("hi: "+str(hi))
            #print("i: "+str(i))
            list_one.update({gi:i})
            list_two.update({hi:i})
            i+=1

        for huk in list_two.keys():
            for gk in list_one.keys():
                if huk == gk:
                    #print("final i,j: "+str(i)+","+str(list_two.get(huk)))
                    return list_one.get(gk) + (list_two.get(huk) * n)
        print(str((intv/check_interval)*100)+"% completed")
