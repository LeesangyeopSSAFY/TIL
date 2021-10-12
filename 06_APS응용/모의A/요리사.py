# case는 각 경우의 수의 배열 리스트
# synergy함수는 각 조합 리스트에서 식재료 두 개씩 모아놓은 리스트를 반환하기 위해 만든 함수
def synergy(case):
    comb_list = []
    for i in range(1<<(N//2)):
        comb = []
        for j in range(N//2):
            if i & (1<<j):
                comb.append(case[j])
        if len(comb) == 2:
            comb_list.append(comb)
    return comb_list

T = int(input())
for t in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    arr = []
    ans = 987654321
    # arr: 가능한 경우의 수를 만들기 위해 1부터 N까지의 숫자(식재료 번호)가 담긴 리스트
    for i in range(1, N+1):
        arr.append(i)
    tmp_list = []
    #########################
    # tmp_list에는 각 식재료의 조합 리스트가 담긴다
    for i in range(1<<N):
        tmp = []
        for j in range(N):
            if i & (1<<j):
                tmp.append(arr[j])
        if len(tmp) == N // 2:
            tmp_list.append(tmp)
    #########################
    # tmp_list에서 처음과 끝, 2번째와 마지막 2번째 조합이 서로 합쳐지면 N개의 식재료가 완성되는 것을 알 수 있다
    for idx in range(len(tmp_list)//2):
        S_A = 0
        S_B = 0
        # tmp_list의 각 요소에서 2개씩 조합 가진 식재료의 시너지(synergy함수로 반환된 2개 재료 조합)들을 더해서 S_A에 저장
        combo1 = synergy(tmp_list[idx])
        for i in range(len(combo1)):
            S_A += S[combo1[i][0]-1][combo1[i][1]-1]
            S_A += S[combo1[i][1]-1][combo1[i][0]-1]
        ##################################
        combo2 = synergy(tmp_list[len(tmp_list)-1-idx])
        for i in range(len(combo2)):
            S_B += S[combo2[i][0]-1][combo2[i][1]-1]
            S_B += S[combo2[i][1]-1][combo2[i][0]-1]
        # 만약 두 재료 시너지 차이가 ans보다 작으면 ans 교체
        if abs(S_A - S_B) < ans:
            ans = abs(S_A - S_B)

    print('#{} {}'.format(t, ans))