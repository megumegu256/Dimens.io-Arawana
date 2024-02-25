import rotation  as r
import math

# (2<=n<=12)
n = 3 
# points n
ps = [[0,0,1,2],[0,0],[1,1,1]]
# thetas comb(n,2)
ths = []
# phis comb(n,2)
phs = []
# lines 2
ls = []

# rotation points position
rp = []
# rotation points graphic
rg = []


for i in range(len(ps)):
    if len(ps[i]) != n:
        dfc = n-len(ps[i])
        if dfc > 0:
            ps[i].append(0)
        elif dfc < 0:
            ps[i].pop()


if len(ths) != math.comb(n,2):
    dfc = n-len(ths)
    if dfc > 0:
        ths.append(0)
    elif dfc < 0:
        ths.pop()

if len(phs) != math.comb(n,2):
    dfc = n-len(ths)
    if dfc > 0:
        phs.append(0)
    elif dfc < 0:
        phs.pop()

for j in range(len(ls)):
    if len(ls[j]) != 2:
        dfc = 2-len(ls[j])
        if dfc > 0:
            ls[j].append(0)
        elif dfc < 0:
            ls[j].pop()





print(ps)
