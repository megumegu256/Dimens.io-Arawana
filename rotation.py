import math
import numpy as np

def nrm(n,i,j,x):
    rot = np.identity(n)#
    
    x = math.radians(x)
    s = math.sin(x)
    c = math.cos(x)

    rot[i,i] = c
    rot[i,j] = -s
    rot[j,i] = s
    rot[j,j] = c

    return rot

def lisumnew(n,vn,vm):
    vr = []
    for i in range(math.comb(n,2)):
        vr.append((vn[i]+vm[i])%360)
    return vr

def lisum(n,vn,vm,vl):
    vr = []
    for i in range(math.comb(n,2)):
        vr.append((vn[i]+vm[i]+vl[i])%360)
    return vr
    


def rot(n,pos,vn):
    t = 0
    pos = np.array(pos)
    for i in range(n):
        for j in range(i+1,n):
            rot = nrm(n,i,j,vn[t])
            pos = rot @ pos
            t += 1
    return pos