dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    board = [[0]*(M+K*2) for _ in range(N+K*2)]
    first_status = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if first_status[i][j] > 0:
                X = first_status[i][j]
                board[K+i][K+j] = [X, X, X, 0]
    
    for k in range(K+1):
        for r in range(len(board)):
            for c in range(len(board[0])):
                if type(board[r][c]) == list:
                    if board[r][c][0] > 0 and board[r][c][3] != k: # 비활성화 상태이면
                        board[r][c][0] -= 1
                    elif board[r][c][0] == 0 and board[r][c][1] > 0: #비활성 상태가 끝나고 활성 상태라면
                        vitality = board[r][c][2] # 번식하는 줄기 세포의 생명력 수치
                        board[r][c][1] -= 1
                        for dir in range(4):
                            nr = r + dr[dir]
                            nc = c + dc[dir]
                            if board[nr][nc] == 0: # 줄기세포가 없는 셀이라면
                                board[nr][nc] = [vitality, vitality, vitality, k]
                            else:
                                # if board[nr][nc][0] == board[nr][nc][1] == board[nr][nc][2] and vitality > board[nr][nc][2]: # 동시에 번식하는 줄기 세포 중 생명력 수치가 더 낮은 경우
                                if board[r][c][3] == k and vitality > board[nr][nc][2]: # 동시에 번식하는 줄기 세포 중 생명력 수치가 더 낮은 경우
                                    board[nr][nc] = [vitality, vitality, vitality, k]

    ans = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if type(board[i][j]) == list:
                if board[i][j][1] > 0:
                    ans += 1
    
    print('#{} {}'.format(t, ans))
    # print(board)

    
    

