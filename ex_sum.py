for t in range(10):
    big_list = []
    tc_num = input()
    # 100*100의 2차원 배열 받기
    for list_input in range(100):
        big_list.append(list(map(int, input().strip().split())))

    maxi = 0
    total_list = []
    total_dk1 = 0
    total_dk2 = 0
    for r in range(100):
        total_c = 0
        total_r = 0
        # (0,0)부터 (99,99)까지의 대각선의 합
        total_dk1 += big_list[r][r]
        # (0,99)부터 (99,0)까지의 대각선의 합
        total_dk2 += big_list[r][100-1-r]
        for c in range(100):
            # 각 열의 합 구하기
            total_c += big_list[c][r]
            # 각 행의 합 구하기
            total_r += big_list[r][c]
        total_list.append(total_c)
        total_list.append(total_r)
    total_list.append(total_dk1)
    total_list.append(total_dk2)

    # 각 행, 열, 대각선의 합 중 최댓값 구하기
    maxi = total_list[0]
    for ch_total in total_list:
        if ch_total >= maxi:
            maxi = ch_total

    print("#{} {}".format(tc_num, maxi))