T = int(input())
for t in range(1, T+1):
    N = int(input())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    # 종료 시간을 기준으로 오름차순 정렬하기
    A.sort(key=lambda x:x[1])
    # 이용할 화물차 목록
    S = [A[0]]
    j = 0
    for i in range(1, N):
        # 시작 시간이 그 전 종료 시간보다 같거나 크면
        if A[i][0] >= A[j][1]:
            S.append(A[i])
            # j를 i로 갱신
            j = i

    print('#{} {}'.format(t, len(S)))