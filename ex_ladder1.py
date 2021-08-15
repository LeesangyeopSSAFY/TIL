for _ in range(1):
    tc = int(input())
    baekbaek = []
    for t_input in range(100):
        baekbaek.append(list(map(int, input().strip().split())))

    for find_2 in range(100):
        if baekbaek[99][find_2] == 2:
            g_idx = find_2

    r = 99
    c = g_idx
    d = 0
    while r > 0:
        if (0 < c < 100) and (d == 0 or d == 1) and baekbaek[r][c-1]:
            c -= 1
            d = 1
        elif (0 < c < 100) and (d == 0 or d == 2) and baekbaek[r][c+1]:
            c += 1
            d= 2
        else:
            r -= 1
            d = 0

    print("#{} {}".format(tc, c))