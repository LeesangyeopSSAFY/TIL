# 유기농 배추
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    global cnt
    Q = [(r, c)]
    visited[r][c] = 1
    
    while Q:
        curr_r, curr_c = Q.pop(0)
        for dir in range(4):
            nr = curr_r + dr[dir]
            nc = curr_c + dc[dir]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if ground[nr][nc] == 1 and visited[nr][nc] == 0:
                Q.append((nr, nc))
                visited[nr][nc] = 1
    # bfs를 다 끝내고 난 후 cnt 하나 추가해서 배추흰지렁이 수 카운트
    cnt += 1
    return cnt




T = int(input())
for t in range(1, T+1):
    M, N, K = map(int, input().split())
    ground = [[0] * M for _ in range(N)]
    for k in range(K):
        X, Y = map(int, input().split())
        ground[Y][X] = 1
    
    visited = [[0] * M for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
    print(cnt)
