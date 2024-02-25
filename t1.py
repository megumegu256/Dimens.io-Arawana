import math
n = 3
ths = [0]




while len(ths) != math.comb(n,2):
    dfc = n-len(ths)
    if dfc > 0:
        ths.append(0)
    elif dfc < 0:
        ths.pop()

print(ths)