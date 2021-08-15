T = int(input())
cnt = 0
for t in range(T):
    cnt += 1
    nn = []
    nk = list(map(int, input().split()))
    N = nk[0]
    K = nk[1]
    # N*N 행렬의 테두리에 0을 둘러쌈
    nn.append([0] * (N + 2))
    for n in range(N):
        nn.append([0] + list(map(int, input().split())) + [0])
    nn.append([0] * (N + 2))
    
    total = 0
    for rc in range(1, N-K+2): # 구간합 구하듯 K 길이만큼을 구하기 위해 1부터 N-K+1까지
        for i in range(1, N+1):
            row_cnt = 0
            col_cnt = 0
            for k in range(K):
                if nn[i][rc+k] == 1:
                    col_cnt += 1
                if nn[rc+k][i] == 1:
                    row_cnt += 1
            # 만약 K번 동안 1이고 그 앞뒤로 0일 경우 total에 1씩 추가
            if row_cnt == K and nn[rc-1][i] == 0 and nn[rc+K][i] == 0:
                total += 1
            if col_cnt == K and nn[i][rc-1] == 0 and nn[i][rc+K] == 0:
                total += 1
    
    print("#{} {}".format(cnt, total))