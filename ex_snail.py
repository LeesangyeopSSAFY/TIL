T = int(input())
for t in range(1, T+1):
    N = int(input())
    box = []
    for n in range(N):
        box.append([0]*N)

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    value = 1
    r, c = 0, -1
    k = 0

    while value <= N*N:
        nr = r + dr[k]
        nc = c + dc[k]
        if (0 <= nr < N) and (0 <= nc < N) and (box[nr][nc] == 0):
            box[nr][nc] = value
            value += 1
            r, c = nr, nc
        else:
            k = (k+1) % 4

    print("#{}".format(t))
    for jull in box:
        for gab in jull:
            print("{}".format(gab), end=" ")
        print()