import math
import numpy as np



def nrm(i,j,x):
    rot = np.identity(n)#
    
    x = math.radians(x)
    s = math.sin(x)
    c = math.cos(x)

    rot[i,i] = c
    rot[i,j] = -s
    rot[j,i] = s
    rot[j,j] = c

    return rot

def rot(pos,vn):
    t = 0
    pos = np.array(pos)
    for i in range(n):
        for j in range(i+1,n):
            rot = nrm(i,j,vn[t])
            pos = rot @ pos
            t += 1
    return pos

n = 4

#n
# tmp = [1,1,1,1] 点(x,y,z,w)

#comb(n,2)
# vn = [0,0,0,30,0,0] 角度(t0,t1,t2,t3,t4,t5) theta

# vn() = [0,0,0,0,0,0] 角度(p0,p1,p2,p3,p4,p5) phi

# print(rot(tmp,vn))