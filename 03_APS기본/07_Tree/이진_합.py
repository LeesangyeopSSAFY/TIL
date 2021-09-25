T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [0] * (N+1)
    val_list = list(map(int, input().split()))
    arr[1] = val_list[0] # 우선 첫 번째 값 집어넣은 후
    for n in range(2, N+1):
        arr[n] = val_list[n-1]
        if arr[n] < arr[n//2]: # 만약 넣을 값보다 부모 노드의 값이 더 크다면
            while arr[n] < arr[n//2]: # 부모 노드의 값이 더 작을 때까지
                arr[n//2], arr[n] = arr[n], arr[n//2] # 자리 바꿈
                n = n // 2

    ans = 0
    while N >= 1:
        ans += arr[N//2] # 조상 노드에 저장된 정수의 합 구하기
        N = N//2
    print('#{} {}'.format(t, ans))