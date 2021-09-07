dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(r, c, color):
    Q = [(r, c)]
    visited[r][c] = color
    cnt = 0

    while Q:
        curr_r, curr_c = Q.pop(0)
        cnt += 1
        for dir in range(4):
            nr = curr_r + dr[dir]
            nc = curr_c + dc[dir]

            if nr < 0 or nr >= N or nc < 0 or nc >= N: # 범위 체크
                continue
            if arr[nr][nc] == '1' and visited[nr][nc] == 0:
                Q.append((nr, nc))
                visited[nr][nc] = color
    return cnt
    



N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
ans = []
color = 1

for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and visited[i][j] == 0:
            homes = BFS(i, j, color)
            ans.append(homes)
            color += 1

ans.sort()
print(len(ans))
for a in ans:
    print(a)