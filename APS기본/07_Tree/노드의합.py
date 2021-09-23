T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [0] * (N+1)
    for _ in range(M):
        ind, val = map(int, input().split())
        arr[ind] = val

    if N % 2 == 0: # 짝수일 때
        arr[N//2] = arr[N] # 자식 노드가 한 개인 값을 부모 노드에 저장
        for n in range(N-1, 0, -2):
            arr[n//2] = arr[n-1] + arr[n] # 자식 노드의 합을 부모 노드에 저장
    else:
        for n in range(N, 0, -2):
            arr[n//2] = arr[n-1] + arr[n]

    print('#{} {}'.format(t, arr[L]))