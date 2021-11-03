def sudoku(r, c):
    for i in range(9):
        if arr[i][c] != 0 and r_vis[arr[i][c]] == 0:
            r_vis[arr[i][c]] = 1

    for j in range(9):
        if arr[r][j] != 0 and c_vis[arr[r][j]] == 0:
            c_vis[arr[r][j]] = 1

    str = (r // 3) * 3
    stc = (c // 3) * 3
    for i in range(3):
        for j in range(3):
            if arr[str+i][stc+j] != 0 and nemo_vis[arr[str+i][stc+j]] == 0:
                nemo_vis[arr[str+i][stc+j]] = 1

    for i in range(1, 10):
        if r_vis[i] == 0 and c_vis[i] == 0 and nemo_vis[i] == 0:
            return i



arr = [list(map(int, input().split())) for _ in range(9)]
r_vis = [1] + [0] * 9
c_vis = [1] + [0] * 9
nemo_vis = [1] + [0] * 9

for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            arr[i][j] = sudoku(i, j)
            r_vis = [1] + [0] * 9
            c_vis = [1] + [0] * 9
            nemo_vis = [1] + [0] * 9

for i in range(9):
    print(*arr[i])