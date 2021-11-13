from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    Q = deque()
    Q.append((r, c))
    visited[r][c] = 1
    while Q:
        cn, cc = Q.popleft()
        for dir in range(4):
            nr = cn + dr[dir]
            nc = cc + dc[dir]
            if 0<=nr<M and 0<=nc<N:
                if zido[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    Q.append((nr, nc))

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    zido = [[0] * N for _ in range(M)]
    for _ in range(K):
        r, c = map(int, input().split())
        zido[r][c] = 1

    visited = [[0]*N for _ in range(M)]
    worm = 0
    for i in range(M):
        for j in range(N):
            if zido[i][j] and not visited[i][j]:
                bfs(i, j)
                worm += 1

    print(worm)