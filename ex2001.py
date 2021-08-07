T = int(input())
for t in range(T):
    NM_list = list(map(int, input().split()))
    N = int(NM_list[0])
    M = int(NM_list[1])
    NN_list = []
    for n in range(N):
        NN_list.append(list(map(int, input().split())))

    max_val = 0
    total = 0
    totals = []
    for i in range(N - M + 1):
        sum_total = 0
        for j in range(N - M + 1):
            for k in range(M):
                total = sum(NN_list[i+k][j:j+M])
            totals.append(total)
            total = 0

    print(totals)
