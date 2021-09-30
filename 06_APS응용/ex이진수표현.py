TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    ans = 'ON'
    for n in range(N):
        if M % 2 == 0:
            ans = 'OFF'
        else:
            M = M // 2
    
    print('#{} {}'.format(tc, ans))

