T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [0] * (N+1)
    val_list = list(map(int, input().split()))
    arr[1] = val_list[0]
    # 1부터 노드 번호가 시작되므로 arr은 2부터, val_list는 1번 인덱스부터
    for n in range(2, N+1):
        arr[n] = val_list[n-1]
        # 만약 부모 노드의 값이 넣을 자식 노드의 값보다 크다면
        if arr[n] < arr[n//2]:
            # 부모 노드 값이 더 작을 때까지
            while arr[n] < arr[n//2]:
                arr[n//2], arr[n] = arr[n], arr[n//2]
                n = n//2
    
    ans = 0
    while N >= 1:
        ans += arr[N//2]
        N = N//2
    print('#{} {}'.format(t, ans))

