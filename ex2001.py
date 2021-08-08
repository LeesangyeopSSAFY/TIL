T = int(input())
cnt = 0
for t in range(T):
    cnt += 1
    # N과 M을 입력받는 변수
    NM_list = list(map(int, input().split()))
    N = int(NM_list[0])
    M = int(NM_list[1])
    NN_list = []
    for n in range(N):
        # N*N의 리스트를 받는 변수
        NN_list.append(list(map(int, input().split())))

    total = 0
    totals = []
    # 세로(i)는 N에서 M을 뺀 길이만큼 순회
    for i in range(N - M + 1):
        sum_total = 0
        # 가로(j) 역시 N에서 M을 뺀 길이만큼 순회
        for j in range(N - M + 1):
            for k in range(M):
                total = sum(NN_list[i+k][j:j+M])
                # totals는 각 행에서 M 길이까지의 합을 나타내는 리스트를 반환
                totals.append(total)
    
    ans_list = []
    for l in range(0, len(totals), M):
        # totals에서 M번째 l에서 l+M까지를 더하면 원하는 사각형 만큼의 합을 구할 수 있음
        ans_list.append(sum(totals[l:l+M]))
        
    print(f'#{cnt} {max(ans_list)}')
