T = int(input())
for t in range(1, T+1):
    N = int(input())
    alpha = [0]*26
    for _ in range(N):
        munza = input()
        if alpha[ord(munza[0])-65] == 0:
            alpha[ord(munza[0]) - 65] = 1
    idx = 0
    cnt = 0
    while alpha[idx] != 0:
        cnt += 1
        idx += 1
    print("#{} {}".format(t, cnt))