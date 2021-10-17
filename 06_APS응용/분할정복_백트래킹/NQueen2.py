import copy


def NQueen(idx, visited):
    global result
    # 마지막 행까지 퀸을 놓을 수 있으면
    if idx == N:
        result += 1
    else:
        for queen in range(N):
            # visited를 변형시키지 않기 위해 deepcopy
            used = copy.deepcopy(visited)
            if used[idx][queen] == 0:
                # 그 행 visited 처리
                used[idx] = [1]*N
                # 열 visited 처리
                for r in range(N):
                    used[r][queen] = 1
                # 대각 visited 처리
                ###############################################
                row1 = idx
                col1 = queen
                while 1<=row1<N+1 and -1<=col1<N-1:
                    row1 -= 1
                    col1 += 1
                    used[row1][col1] = 1
                row2 = idx
                col2 = queen
                while 1<=row2<N+1 and 1<=col2<N+1:
                    row2 -= 1
                    col2 -= 1
                    used[row2][col2] = 1
                row3 = idx
                col3 = queen
                while -1<=row3<N-1 and 1<=col3<N+1:
                    row3 += 1
                    col3 -= 1
                    used[row3][col3] = 1
                row4 = idx
                col4 = queen
                while -1<=row4<N-1 and -1<=col4<N-1:
                    row4 += 1
                    col4 += 1
                    used[row4][col4] = 1
                ##############################################

                NQueen(idx+1, used)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    visited = [[0]*N for _ in range(N)]
    result = 0
    NQueen(0, visited)
    print('#{} {}'.format(t, result))