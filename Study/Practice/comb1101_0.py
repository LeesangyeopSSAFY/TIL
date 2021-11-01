def nCr(s, k):
    if k == r:
        print(*comb)
    else:
        for i in range(s, n-r+k+1):
            comb[k] = i
            nCr(i+1, k+1)

def comb1(idx, s_idx):
    if s_idx == r:
        print(*sel)
        return
    
    for i in range(idx, n):
        sel[s_idx] = i
        comb1(i+1, s_idx+1)

n = 6
r = 3
sel = [0] * r
comb = [0] * r
# comb1(0, 0)
nCr(0, 0)