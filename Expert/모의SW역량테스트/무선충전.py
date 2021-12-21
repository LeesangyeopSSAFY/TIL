dr = [0, -1, 0, 1, 0]
dc = [0, 0, 1, 0, -1]

T = int(input())
for t in range(1, T+1):
    M, A = map(int, input().split())
    userA = list(map(int, input().split()))
    userB = list(map(int, input().split()))
    AP_list = [list(map(int, input().split())) for _ in range(A)]
    m_case = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]] # 이동하지 않음, 상, 우, 하, 좌
    a_idx = [0, 0]
    b_idx = [9, 9]

    charging = 0

    idx = -1
    while idx != M:
        tmp_charging = 0 # 현재 최대 충전 값
        a_cr, a_cc = a_idx
        b_cr, b_cc = b_idx

        for w in range(A):
            w_r, w_c, w_C, w_P = AP_list[w]
            tmp_A = 0

            if abs(w_r - a_cr - 1) + abs(w_c - a_cc - 1) <= w_C:
                tmp_A += w_P

            for e in range(A):
                e_r, e_c, e_C, e_P = AP_list[e]
                tmp_B = 0
                if abs(e_r - b_cr - 1) + abs(e_c - b_cc - 1) <= e_C:
                    # 같은 BC 조건으로 확인하고, a도 그 BC안에 있으면
                    # BC를 나눠 갖는데, 이미 a에서 더했으므로 더할 필요가 없다
                    if w == e and tmp_A != 0:
                        pass
                    else:
                        tmp_B += e_P

                if tmp_charging < tmp_A + tmp_B:
                    tmp_charging = tmp_A + tmp_B
        
        idx += 1

        if idx != M:
            a_idx = [a_idx[0] + dc[userA[idx]], a_idx[1] + dr[userA[idx]]]
            b_idx = [b_idx[0] + dc[userB[idx]], b_idx[1] + dr[userB[idx]]]

        charging += tmp_charging
    
    print('#{} {}'.format(t, charging))