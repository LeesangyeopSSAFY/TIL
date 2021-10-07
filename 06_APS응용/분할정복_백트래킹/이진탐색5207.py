def binarySearch(A, b):
    global ans
    l = 0
    r = N-1
    dir = ''
    while l <= r:
        mid = int((l+r)/2)
        if A[mid] == b:
            ans += 1
            return
        # 오른쪽 탐색해야 할 때
        elif A[mid] < b:
            # 전도 오른쪽 탐색일 때
            if dir == 'right':
                break
            l = mid + 1
            dir = 'right'
        # 왼쪽 탐색해야 할 때
        else:
            # 전도 왼쪽 탐색일 때
            if dir == 'left':
                break
            r = mid - 1
            dir = 'left'
    return


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    ans = 0
    for b in B:
        binarySearch(A, b)

    print('#{} {}'.format(t, ans))