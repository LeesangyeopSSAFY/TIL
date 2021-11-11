from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    houseCnt = 1
    Q = deque()
    Q.append((r, c))
    visited[r][c] = danjiNum
    zido[r][c] = 0
    while Q:
        curr_r, curr_c = Q.popleft()

        for dir in range(4):
            nr = curr_r + dr[dir]
            nc = curr_c + dc[dir]

            if nr<0 or nr>=N or nc<0 or nc>= N:
                continue

            if not visited[nr][nc] and zido[nr][nc]:
                visited[nr][nc] = danjiNum
                zido[nr][nc] = 0
                houseCnt += 1
                Q.append((nr, nc))
    return houseCnt

N = int(input())
zido = [[] for _ in range(N)]
for r in range(N):
    tmp = input()
    for t in tmp:
        zido[r].append(int(t))

ans_list = []
visited = [[0]*N for _ in range(N)]
danjiNum = 0

for i in range(N):
    for j in range(N):
        if zido[i][j] == 1:
            ans_list.append(bfs(i, j))
            danjiNum += 1

ans_list.sort()
print(danjiNum)
for ans in ans_list:
    print(ans)