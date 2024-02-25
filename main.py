import rotation  as r
import math

# (2<=n<=12)
n = 3 

# points n
ps = []
# thetas comb(n,2)
ths = []
# phis comb(n,2)
phs = []
# rotation variation comb(n,2)
rv = []
# psi comb(n,2)
pss = []

# lines 2
ls = []

# rotation points position
rp = []
# rotation points graphic
rg = []



for i in range(len(ps)):
    while len(ps[i]) != n:
        dfc = n-len(ps[i])
        if dfc > 0:
            ps[i].append(0)
        elif dfc < 0:
            ps[i].pop()


while len(ths) != math.comb(n,2):
    dfc = n-len(ths)
    if dfc > 0:
        ths.append(0)
    elif dfc < 0:
        ths.pop()

while len(phs) != math.comb(n,2):
    dfc = n-len(phs)
    if dfc > 0:
        phs.append(0)
    elif dfc < 0:
        phs.pop()

while len(rv) != math.comb(n,2):
    dfc = n-len(rv)
    if dfc > 0:
        phs.append(0)
    elif dfc < 0:
        phs.pop()

while len(pss) != math.comb(n,2):
    dfc = n-len(pss)
    if dfc > 0:
        phs.append(0)
    elif dfc < 0:
        phs.pop()

for m in range(math.comb(n,2)):
    pss[m] += rv[m]

for j in range(len(ls)):
    while len(ls[j]) != 2:
        dfc = 2-len(ls[j])
        if dfc > 0:
            ls[j].append(0)
        elif dfc < 0:
            ls[j].pop()


while len(rp) != len(ps):
    dfc = n-len(rp)
    if dfc > 0:
        rp.append(0)
    elif dfc < 0:
        rp.pop()

while len(rg) != len(ps):
    dfc = n-len(rg)
    if dfc > 0:
        rg.append(0)
    elif dfc < 0:
        rg.pop()


for k in range(len(ps)):
    rp[k] = r.rot(n,ps[k],ths)

for l in range(len(ps)):
    rg[l] = r.rot(n,ps[l],r.lisum(n,ths,phs,pss))
