# Title: Extended Euclidean Algorithm
# Creator: Austin Akerley
# Date Created: 11/26/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/18/2020
# Associated Book Page Nuber: 16

# INPUT -
# x - type: int, desc: one of the inputs for the extended euclidean algorithm
# y - type: int, desc: one of the inputs for the extended euclidean algorithm

def eea(x, y): # gcd(x,y) = ax + by
    flipped = False
    if x==0 or y==0:
        return {"gcd":0, "a":0, "x":0, "b":0, "y":0}
    elif x==y:
        return [x, 2, x -1, y]
    elif x < y: # set x to be the bigger number
        flipped = True
        tmp=x
        x=y
        y=tmp
    #Start of real algorithm
    starting_x = x
    starting_y = y
    q = [0, 0]
    r = [x, y]
    s = [1, 0]
    t = [0, 1]
    remainder = None
    i=1
    while remainder != 0:
        i+=1
        quotient = int(x/y)
        remainder = x%y
        q.append(quotient)
        r.append(remainder)
        x=y
        y=remainder
        s.append(s[i-2]-(s[i-1]*q[i-1]))
        t.append(t[i-2]-(t[i-1]*q[i-1]))
    if flipped:
        return {"gcd":r[i-1], "a":s[i], "x":starting_x, "b":t[i], "y":starting_y}
    else:
        return {"gcd":r[i-1], "a":t[i], "x":starting_x, "b":s[i], "y":starting_y}

    # OUTPUT - type: dictionary
    # {
    #     "gcd" - type: int, desc: gcd(x, y),
    #     "a" - type: int, desc: a,
    #     "x" - type: int, desc: x,
    #     "b" - type: int, desc: b,
    #     "y" - type: int, desc: y
    # }
