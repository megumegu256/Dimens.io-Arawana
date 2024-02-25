import rotation  as r
import math

# (2<=n<=12)
n = 3 

# points n 初期座標
ps = [[0],[1],[2]]
# thetas comb(n,2) 初期回転角度
ths = []
# phis comb(n,2) 軸回転角度
phs = []
# rotation variation comb(n,2) 回転速度
rv = []
# psi comb(n,2) 
pss = []

# lines 2 線入力
ls = []


# rotation points position 回転後座標
rp = []
# rotation points new 回転後座標(速度変化あり)
rn = []
# rotation points graphic 回転後座標(速度、軸変化あり)
rg = []



for i in range(len(ps)):
    while len(ps[i]) != n:
        dfc = n-len(ps[i])
        if dfc > 0:
            ps[i].append(0)
        elif dfc < 0:
            ps[i].pop()


while len(ths) != math.comb(n,2):
    dfc = math.comb(n,2)-len(ths)
    if dfc > 0:
        ths.append(0)
    elif dfc < 0:
        ths.pop()

while len(phs) != math.comb(n,2):
    dfc = math.comb(n,2)-len(phs)
    if dfc > 0:
        phs.append(0)
    elif dfc < 0:
        phs.pop()

while len(rv) != math.comb(n,2):
    dfc = math.comb(n,2)-len(rv)
    if dfc > 0:
        rv.append(0)
    elif dfc < 0:
        rv.pop()

while len(pss) != math.comb(n,2):
    dfc = math.comb(n,2)-len(pss)
    if dfc > 0:
        pss.append(0)
    elif dfc < 0:
        pss.pop()

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
    dfc = len(ps)-len(rp)
    if dfc > 0:
        rp.append(0)
    elif dfc < 0:
        rp.pop()

while len(rn) != len(ps):
    dfc = len(ps)-len(rn)
    if dfc > 0:
        rn.append(0)
    elif dfc < 0:
        rn.pop()

while len(rg) != len(ps):
    dfc = len(ps)-len(rg)
    if dfc > 0:
        rg.append(0)
    elif dfc < 0:
        rg.pop()


for k in range(len(ps)):
    rp[k] = r.rot(n,ps[k],ths)

for o in range(len(ps)):
    rn[o] = r.rot(n,ps[o],r.lisumnew(n,ths,phs))

for l in range(len(ps)):
    rg[l] = r.rot(n,ps[l],r.lisum(n,ths,phs,pss))

vr = r.lisum(n,ths,phs,pss) #最終角度



x_data = []
y_data = []


while len(x_data) != len(rg):
    dfc = len(rg)-len(x_data)
    if dfc > 0:
        x_data.append(0)
    elif dfc < 0:
        x_data.pop()

while len(y_data) != len(rg):
    dfc = len(rg)-len(y_data)
    if dfc > 0:
        y_data.append(0)
    elif dfc < 0:
        y_data.pop()


for n in range(len(rg)):
    x_data[n] = rg[n][0]
    y_data[n] = rg[n][1]

print(rg)
print(x_data)
print(y_data)
