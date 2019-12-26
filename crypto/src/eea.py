# Author: Austin Akerley
# Date Last Edited: 12/25/2019
#

# INPUTS: int, int
# x : int
# y : int

def eea(x, y): # gcd(x,y) = ax + by   return value will be a dictionary
    flipped = False
    if x==0 or y==0:
        return {"gcd":0, "a":0, "x":0, "b":0, "y":0}
    elif x==y:
        return [x, 2, x -1, y]
    elif x < y: #X must be greater than y
        flipped = True
        tmp=x
        x=y
        y=tmp
    #Start of real algorithm
    old_x = x
    old_y = y
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
        return {"gcd":r[i-1], "a":s[i], "x":old_y, "b":t[i], "y":old_x}
    else:
        return {"gcd":r[i-1], "a":t[i], "x":old_x, "b":s[i], "y":old_y}

    # OUTPUTS: dictionary
    # {
    #     "gcd" : gcd(x, y),
    #     "a" : a,
    #     "x" : x,
    #     "b" : b,
    #     "y" : y
    # }
