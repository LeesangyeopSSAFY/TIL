def N_and_M(idx):
    if idx == M:
        tmp = sorted(arr)
        if tmp in double_check:
            return
        double_check.append(tmp)
        print(*tmp)
        return

    for i in range(N):
        if not used[i]:
            used[i] = 1
            arr[idx] = i + 1
            N_and_M(idx+1)
            used[i] = 0

N, M = map(int, input().split())
arr = [0 for _ in range(M)]
used = [0] * N
double_check = []

N_and_M(0)
