def powerset(idx):
    if idx == N:
        print(*sel)
        return
    
    sel[idx] = 1
    powerset(idx+1)
    sel[idx] = 0
    powerset(idx+1)

N = 3
arr = [1, 2, 3]

sel = [0] * N

# powerset(0)

for i in range(1<<N):
    tmp = []
    for j in range(N):
        if i & (1<<j):
            tmp.append(arr[j])
    print(*tmp)
