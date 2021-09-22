T = int(input())
for t in range(1, T+1):
    N = int(input())
    box = [[0]*N for _ in range(N)]
    print(box)

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    value = 1
    r, c = 0, -1 #c가 -1부터 시작하는 이유는 (0, 0)부터 시작하기 때문에
    k = 0

    while value <= N*N:
        nr = r + dr[k]
        nc = c + dc[k]
        if (0<= nr < N) and (0 <= nc < N) and (box[nr][nc] == 0): #벽을 만나기 전
            box[nr][nc] = value
            value += 1
            r, c = nr, nc
        else: # 벽을 만나서 회전해야 할 때
            k = (k+1) % 4
    
    print("#{}".format(t))
    for jull in box:
        for ans in jull:
            print(ans, end=" ")
        print()