dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 각 터널 구조물 타입 별 갈 수 있는 방향
pipe = [
    [],
    [0, 1, 2, 3],
    [1, 3],
    [0, 2],
    [0, 3],
    [0, 1],
    [1, 2],
    [2, 3]
]

T = int(input())
for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    Q = [(R, C, 1)]
    visited[R][C] = 1

    ans = 0

    while Q:
        r, c, time = Q.pop(0)
        ans += 1
        if time >= L:
            continue

        curr_p = tunnel[r][c]
        for i in pipe[curr_p]:
            nr = r + dr[i]
            nc = c + dc[i]
            # 범위 체크
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            # 터널이 없거나 방문헀던 곳이라면 패스
            if tunnel[nr][nc] == 0 or visited[nr][nc]:
                continue
            # nr, nc에서 연결되어 있으면
            if (i + 2) % 4 in pipe[tunnel[nr][nc]]: # (i+2)%4를 하면 상하, 좌우처럼 서로 연결되는 곳이 있는지 확인할 수 있다.
                Q.append((nr, nc, time+1))
                visited[nr][nc] = 1

    print('#{} {}'.format(t, ans))