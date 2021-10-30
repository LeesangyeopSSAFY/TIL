def N_and_M(sel_idx, arr_idx):
    if sel_idx == M:
        print(*sel)
    else:
        for idx in range(arr_idx, N - M + sel_idx + 1):
            if not visited[idx]:
                visited[idx] = 1
                sel[sel_idx] = arr[idx]
                N_and_M(sel_idx+1, arr_idx+1)
                visited[idx] = 0

N, M = map(int, input().split())
arr = [0 for _ in range(N)]


N_and_M(0, 0)
