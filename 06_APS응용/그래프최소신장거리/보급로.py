from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def restore():
    Q = deque()
    Q.append((0, 0))
    times[0][0] = 0
    while Q:
        r, c = Q.popleft()
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if times[nr][nc] > times[r][c] + arr[nr][nc]:
                times[nr][nc] = times[r][c] + arr[nr][nc]
                Q.append((nr, nc))


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    for n in range(N):
        tmp = input()
        for i in range(N):
            arr[n][i] = int(tmp[i])
    times = [[987654321] * N for _ in range(N)]
    restore()
    ans = times[N-1][N-1]

    print('#{} {}'.format(t, ans))