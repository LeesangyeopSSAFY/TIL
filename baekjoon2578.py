# 빙고
def BINGO(arr):
    bingo = 0
    for garo in arr:
        if garo == [0] * 5:
            bingo += 1
    # for r in range(5):
    #     cnt_r = 0
    #     for k in range(5):
    #         if arr[r][k] == 0:
    #             cnt_r += 1
    #     if cnt_r == 5:
    #         bingo += 1

    for c in range(5):
        cnt = 0
        for k in range(5):
            if arr[k][c] == 0:
                cnt += 1
        if cnt == 5:
            bingo += 1

    if arr[0][0] == 0 and arr[1][1] == 0 and arr[2][2] == 0 and arr[3][3] == 0 and arr[4][4] == 0:
        bingo += 1
    if arr[0][4] == 0 and arr[1][3] == 0 and arr[2][2] == 0 and arr[3][1] == 0 and arr[4][0] == 0:
        bingo += 1
    return bingo

plate = []
for i in range(5):
    plate.append(list(map(int, input().split())))

cklist = []
for j in range(5):
    cklist += map(int, input().split())


for a in range(25):
    for r in range(5):
        for c in range(5):
            if plate[r][c] == cklist[a]:
                plate[r][c] = 0
    if BINGO(plate) >= 3:
        print(a+1)
        break