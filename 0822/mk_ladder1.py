for _ in range(10):
    tc = int(input())
    baekbaek = []
    for _ in range(100):
        baekbaek.append(list(map(int, input().strip().split())))

    for find_g in range(100):
        if baekbaek[99][find_g] == 2:
            g_idx = find_g
    
    r = 99
    c = g_idx
    d = 0
    while r > 0:
        if (d==0 or d==1) and c>0 and baekbaek[r][c-1]:
            c -= 1
            d =1
        elif (d==- or d==2) and c < 99 and baekbaek[r][c+1]:
            c += 1
            d = 2
        else:
            r -= 1
            d = 0

    print("#{} {}".formattc, c)