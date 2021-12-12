from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    while Q:
        r, c = Q.popleft()
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if 0<=nr<N and 0<=nc<M:
                if box[nr][nc] == 0:
                    box[nr][nc] = box[r][c] + 1
                    Q.append((nr, nc))

M, N = map(int, input().split())
box = []
for _ in range(N):
    box.append(list(map(int, input().split())))
Q = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            Q.append((i, j))
bfs()
ans = 0
for i in range(N):
    for j in range(M):
        if box[i][j] > 1 and box[i][j] > ans:
            ans = box[i][j] - 1
        elif box[i][j] == 0:
            ans = -1
            break
    if ans == -1:
        break

print(ans)