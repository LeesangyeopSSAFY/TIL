dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    live = [[0]*(M + K*2 + 2) for _ in range(N + K*2 + 2)]
    check = [[0]*(M + K*2 + 2) for _ in range(N + K*2 + 2)]
    for i in range(N):
        data = list(map(int, input().split()))
        for j in range(M):
            live[i][j] = data[j]
            if data[j] > 0:
                check[i][j] = -(data[j])
    
    for _ in range(K):
        board = [[0]*(M+K*2+2) for _ in range(N+K*2+2)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if live[i][j] == 0 or live[i][j] == -1:
                    continue
                if check[i][j] < 0:
                    if check[i][j] == -1:
                        check[i][j] = live[i][j]
                    else:
                        check[i][j] += 1
                elif check[i][j] > 0:
                    r, c = i, j
                    for dir in range(4):
                        nr = (r+dr[dir]) % (N+K*2+2)
                        nc = (c+dc[dir]) % (M+K*2+2)
                        if live[nr][nc] == -1 or live[nr][nc] > 0:
                            continue
                        if board[nr][nc] == 0:
                            board[nr][nc] = live[r][c]
                            check[nr][nc] = -live[r][c]
                        elif board[nr][nc] < live[r][c]:
                            board[nr][nc] = live[r][c]
                            check[nr][nc] = -live[r][c]
                    if check[i][j] == 1:
                        live[i][j] = -1
                        check[i][j] = 0
                    else:
                        check[i][j] -= 1
        
        for i in range(N+K*2+2):
            for j in range(M+K*2+2):
                if board[i][j] > 0 and live[i][j] == 0:
                    live[i][j] = board[i][j]
    
    ans = 0
    for i in range(N+K*2+2):
        for j in range(M+K*2+2):
            if check[i][j] != 0:
                ans += 1
    
    print('#{} {}'.format(t, ans))

