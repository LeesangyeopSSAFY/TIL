def min_sum(r, c, tmp):
    global ans
    # 맨 오른쪽 아래에 도달했을 때
    if (r, c) == (N-1, N-1):
        # tmp값 더해주고
        tmp += plate[r][c]
        # 비교
        if tmp <= ans:
            ans = tmp
        return
    # 범위 비교
    if r >= N or c >= N:
        return
    else:
        min_sum(r+1, c, tmp+plate[r][c])
        min_sum(r, c+1, tmp+plate[r][c])

T = int(input())
for t in range(1, T+1):
    N = int(input())
    plate = []
    for _ in range(N):
        plate.append(list(map(int, input().split())))

    ans = 987654321

    min_sum(0, 0, 0)
    print('#{} {}'.format(t, ans))