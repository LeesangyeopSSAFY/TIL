TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    ans = 'ON'
    # N번만큼 돌면서
    for n in range(N):
        # M을 2로 나눈 나머지가 0이면 즉, 1이 아니면
        if M % 2 == 0:
            # OFF로 바꿈
            ans = 'OFF'
        # 아니면 M 나누기 2
        else:
            M = M // 2
    
    print('#{} {}'.format(tc, ans))

