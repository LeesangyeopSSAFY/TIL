# 90도 회전하는 함수
def mk_90(lists):
    list_90 = []
    # 행부터 내림차순 반복 후 열 오름차순 변경
    for c in range(len(lists)):
        list_r = []
        for r in range(len(lists)-1, -1, -1):
            list_r.append(lists[r][c])
        # join함수를 통해 출력물의 경우 열 사이의 공백을 제거(ex)['741', '852', '963']
        list_90.append(''.join(list_r))
    return list_90

# 180도 회전하는 함수
def mk_180(lists):
    list_180 = []
    # 행부터 내림차순 반복
    for r in range(len(lists)-1, -1, -1):
        list_r = []
        # 열 내림차순 반복
        for c in range(len(lists)-1, -1, -1):
            list_r.append(lists[r][c])
        list_180.append(''.join(list_r))
    return list_180

# 270도 회전하는 함수
def mk_270(lists):
    list_270 = []
    # 열부터 내림차순 반복
    for c in range(len(lists)-1, -1, -1):
        list_r = []
        # 행 오름차순 반복
        for r in range(len(lists)):
            list_r.append(lists[r][c])
        list_270.append(''.join(list_r))
    return list_270


T = int(input())
for t in range(1, T+1):
    N = int(input())
    N_list = []
    for n in range(N):
        N_list.append(list(map(str, input().split())))

    f_ans = mk_90(N_list)
    s_ans = mk_180(N_list)
    t_ans = mk_270(N_list)

    print("#{}".format(t))
    for i in range(N):
        print("{}".format(f_ans[i]), end=" ")
        print("{}".format(s_ans[i]), end=" ")
        print("{}".format(t_ans[i]))
    
