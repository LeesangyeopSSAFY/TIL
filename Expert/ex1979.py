T = int(input())
cnt = 0
for t in range(T):
    cnt += 1
    nn = []
    nk = list(map(int, input().split()))
    N = nk[0]
    K = nk[1]
    nn.append([0] * (N + 2))
    for n in range(N):
        nn.append([0] + list(map(int, input().split())) + [0])
    nn.append([0] * (N + 2))

    total = 0
    for i in range(1, N - K + 2):
        row_cnt = []
        for j in range(1, N - K + 2):
            # 내부 리스트의 j에서 j+K까지가 모두 1이고 그 전값이나 후 값이 0일 경우
            if nn[i][j:j + K] == [1] * K and nn[i][j - 1] == 0 and nn[i][j + K] == 0:
                total += 1
            
            for k in range(K):
                row_cnt.append(nn[i+k][j])
            if row_cnt == [1]*K and nn[i-1][j] == 0 and nn[i+K][j] == 0:
                total += 1

            # if nn[j:j + K + 1][i] == [1] * K and nn[j - 1][i] == 0 and nn[j + K + 1][i] == 0:
            #     total += 1

    print("#{} {}".format(cnt, total))