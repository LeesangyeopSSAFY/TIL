T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    ans = 0
    for i in range(1 << 12):
        cnt_1 = 0
        sum = 0
        for j in range(12):
            if i & (1 << j):
                cnt_1 += 1
                sum += A[j]
        if cnt_1 == N and sum == K:
            ans += 1
    
    print("#{} {}".format(t, ans))