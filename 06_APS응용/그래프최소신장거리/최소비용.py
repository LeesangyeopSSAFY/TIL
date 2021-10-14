dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def fuel():
    Q = [(0, 0)]
    costs[0][0] = 0
    while Q:
        r, c = Q.pop(0)
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if 0<=nr<N and 0<=nc<N:
                # 더 높은 곳으로 갈 때
                if heights[nr][nc] > heights[r][c]:
                    # 비용은 1 + 높이차
                    cost = 1 + heights[nr][nc] - heights[r][c]
                else:
                    cost = 1
                # 가장 작은 값이 costs[nr][nc]에 들어가도록
                if costs[nr][nc] > costs[r][c] + cost:
                    costs[nr][nc] = costs[r][c] + cost
                    Q.append((nr, nc))



T = int(input())
for t in range(1, T+1):
    N = int(input())
    heights = [list(map(int, input().split())) for _ in range(N)]
    costs = [[987654321]*N for _ in range(N)]
    fuel()
    ans = costs[N-1][N-1]

    print('#{} {}'.format(t, ans))