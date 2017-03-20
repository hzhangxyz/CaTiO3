a=3.8822
from math import exp

with open("output","r") as f:
    for i in f:
        p,e = eval(i)
        p[3] -= a/2
        p[4] -= a/2
        p[5] -= a/2
        p = map(lambda x:x/a,p)
        p[0] -= 1 if p[0]>0.5 else 0
        p[1] -= 1 if p[1]>0.5 else 0
        p[2] -= 1 if p[2]>0.5 else 0
        e = exp(-(e+40)/0.0257)
        d = [p[0]*2+p[3], p[1]*2+p[4], p[2]*2+p[5]]
        print e,d

