# 오목판정
T = int(input())
for t in range(1, T+1):
    N = int(input())
    omokpan = []
    for _ in range(N):
        omokpan.append(list(input()))

    ch_garo = False
    for r in range(N):
        for c in range(N-5+1):
            garo = 0
            for o in range(5):
                if omokpan[r][c+o] == 'o':
                    garo += 1
            if garo == 5:
                ch_garo = True
                break

    ch_sero = False
    for c in range(N):
        for r in range(N-5+1):
            cnt = 0
            for o in range(5):
                if omokpan[r+o][c] == 'o':
                    cnt += 1
            if cnt == 5:
                ch_sero = True
                break

    ch_daegak = False
    for r in range(N-5+1):
        for c in range(N-5+1):
            daegak = 0
            for o in range(5):
                if omokpan[r+o][c+o] == 'o':
                    daegak += 1
            if daegak == 5:
                ch_daegak = True
                break

    ch_rdaegak = False
    for r in range(N-5+1):
        for c in range(4, N):
            rdaegak = 0
            for o in range(5):
                if omokpan[r+o][c-o] == 'o':
                    rdaegak += 1
            if rdaegak == 5:
                ch_rdaegak = True
                break



    if ch_garo or ch_sero or ch_daegak or ch_rdaegak:
        print("#{} YES".format(t))
    else:
        print("#{} NO".format(t))