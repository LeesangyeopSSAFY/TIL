def calc(cost, m):
    global min_cost
    # 모든 달을 계산했을 때
    if m > 12:
        # 최소값보다 작으면 교체
        if min_cost > cost:
            min_cost = cost
        return

    # 1일권
    calc(cost + d * month[m], m+1)
    # 1달권
    calc(cost + m1, m+1)
    # 3달권
    calc(cost + m3, m + 3)

T = int(input())
for t in range(1, T+1):
    d, m1, m3, y = map(int, input().split())
    month = [0] + list(map(int, input().split()))

    # 1년 이용권을 min_cost로 우선 설정
    min_cost = y

    calc(0, 1)
    print('#{} {}'.format(t, min_cost))