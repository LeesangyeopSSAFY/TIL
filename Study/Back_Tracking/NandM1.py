def N_and_M(m):
    if m == M:
        print(*sel)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            sel[m] = arr[i]
            N_and_M(m+1)
            visited[i] = 0

N, M = map(int, input().split())
arr = []
for i in range(1, N+1):
    arr.append(i)
visited = [0] * N
sel = [0] * M

N_and_M(0)
