dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def hiking(r, c, road, work):
    global ans
    if road > ans:
        ans = road

    visited[r][c] = 1

    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            # 낮은 곳을 갈 때
            if moutain[r][c] > moutain[nr][nc]:
                hiking(nr, nc, road+1, work)
            elif work and moutain[r][c] > moutain[nr][nc] - K:
                tmp = moutain[nr][nc]
                moutain[nr][nc] = moutain[r][c] - 1
                hiking(nr, nc, road + 1, 0)
                # 원상복구
                moutain[nr][nc] = tmp

    visited[r][c] = 0

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())

    moutain = [list(map(int, input().split())) for _ in range(N)]
    max_h = 0
    # 가장 높은 위치값 찾기
    for i in range(N):
        for j in range(N):
            if max_h < moutain[i][j]:
                max_h = moutain[i][j]

    visited = [[0]*N for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            if moutain[i][j] == max_h:
                hiking(i, j, 1, 1)

    print('#{} {}'.format(t, ans))