T = int(input())
cnt = 0
for t in range(T):
    cnt += 1
    nn = []
    nk = list(map(int, input().split()))
    N = nk[0]
    K = nk[1]
    nn.append([0]*(N+2))
    for n in range(N):
        nn.append([0] + list(map(int, input().split())) + [0])
    nn.append([0]*(N+2))
    
    total1 = 0
    total2 = 0
    for i in range(1, N-K+2):
        for j in range(1, N-K+2):
            if (nn[i][j:j+K] == [1]*K and nn[i][j-1] == 0) or (nn[i][j:j+K] == [1]*K and nn[i][j+K+1] == 0):
                total1 += 1
            
            if (nn[i:i+K][j] == [1]*K and nn[i-1][j] == 0) or (nn[i:i+K][j] == [1]*K and nn[i+K+1][j] == 0):
                total2 += 1
    total = total1 + total2
    print("#{} {}".format(cnt, total))
