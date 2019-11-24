# Author: Austin Akerley
# Date Last Edited: 10/31/2019
#
def eea(x, y): # gcd(x,y) = ax + by   return value will be [GCD, a, x, b, y]
    if x==0 or y==0:
        return [0, 0, 0, 0, 0]
    elif x==y:
        return [x, 2, x -1, y]
    elif x < y: #X must be greater than y
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
    return [r[i-1], t[i], old_x, s[i], old_y]
