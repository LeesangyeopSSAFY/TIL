def DFS(curr, cnt):
    global ans

    for j in range(1, N+1):
        if adjA[curr][j] and not visited[j]:
            visited[j] = 1
            DFS(j, cnt+1)
            visited[j] = 0

    if cnt > ans:
        ans = cnt


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    adjA = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        adjA[x][y] = 1
        adjA[y][x] = 1 # 방향성이 없으므로
    ans = 0
    visited = [False] * (N+1)
    for i in range(1, N+1):
        visited[i] = 1
        DFS(i, 1)
        visited[i] = 0

    print('#{} {}'.format(t, ans))
