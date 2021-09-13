# 섬의 개수

import sys
input = sys.stdin.readline

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]


def bfs(x, y):
    Q = [(x, y)]
    while Q:
        r, c = Q.pop(0)
        for dir in range(8):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if nr < 0 or nr >= h or nc < 0 or nc >= w:
                continue
            if zido[nr][nc] == 1 and visited[nr][nc] == 0:
                Q.append((nr, nc))
                visited[nr][nc] = 1


while True:
    w, h = map(int, input().split())
    if not w and not h:
        break
    zido = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if zido[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                cnt += 1

    print(cnt)