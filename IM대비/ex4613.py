# 러시아 국기 같은 깃발
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    flag = []
    for n in range(N):
        flag.append(list(input()))

    ans_list = []
    for i in range(N-3, -1, -1):
        for j in range(i+1, N-1):
            cnt = 0
            for w in range(0, i+1):
                cnt += M - flag[w].count('W')
            for b in range(i+1, j+1):
                cnt += M - flag[b].count('B')
            for r in range(j+1, N):
                cnt += M - flag[r].count('R')
            ans_list.append(cnt)

    print("#{} {}".format(t, min(ans_list)))