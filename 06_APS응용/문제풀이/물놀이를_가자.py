dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(n, m):
    q = []
    visited = [[0]*M for _ in range(N)]
    cnt = 1
    q.append([n, m])
    while zido[nr][nc] != 'W':
        curr_r, curr_c = q.pop(0)

        for dir in range(4):
            nr = curr_r + dr[dir]
            nc = curr_c + dc[dir]

            if nr < 0 or nr >= N or nc <0 or nc >= M:
                continue
            if zido[nr][nc] == 'L' and not visited[nr][nc]:
                cnt += 1
                visited[nr][nc] = 1
                q.append([nr, nc])
    return cnt



T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    zido = [[0]*M for _ in range(N)]
    for n in range(N):
        line = input()
        for m in range(M):
            zido[n][m] = line[m]

    ans = 0
    for n in range(N):
        for m in range(M):
            if zido[n][m] == 'L':
                ans += bfs(n, m)

    print(ans)
