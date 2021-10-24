T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [0] * (N+1)
    for _ in range(M):
        idx, val = map(int, input().split())
        arr[idx] = val
    
    if N%2 == 0: # N이 짝수일 때
        arr[N//2] = arr[N]
        for n in range(N-1, 0, -2):
            arr[n//2] = arr[n] + arr[n-1]
    else:
        for n in range(N, 0, -2):
            arr[n//2] = arr[n] + arr[n-1]

    print('#{} {}'.format(t, arr[L]))