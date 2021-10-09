dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def DFS(r, c, line):
    # 7자리 완성되면
    if len(line) == 7:
        # ans에 없는 값이라면 넣기
        if line not in ans:
            ans.append(line)
        return

    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]

        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        DFS(nr, nc, line+arr[nr][nc])


T = int(input())
for t in range(1, T+1):
    N = 4
    arr = [input().split() for _ in range(N)]

    ans = []

    for i in range(N):
        for j in range(N):
            DFS(i, j, arr[i][j])

    print('#{} {}'.format(t, len(ans)))