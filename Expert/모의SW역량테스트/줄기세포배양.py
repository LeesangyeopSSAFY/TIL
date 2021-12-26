dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    board = [[0]*(M+K*2) for _ in range(N+K*2)]
    first_status = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            X = first_status[i][j]
            board[K+i][K+j] = [X, X]
    
    
    

