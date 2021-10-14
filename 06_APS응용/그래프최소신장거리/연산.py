from collections import deque

def calc(val):
    Q = deque()
    Q.append(val)
    # 방문쳌 하기 위해 우선 1로 설정하고 ans에서 1빼기
    values[val] = 1
    while Q:
        tmp = Q.popleft()
        # 만약 찾고자 하는 값이 나온다면
        if tmp == M:
            return
        # +1, -1, *2, -10에서
        for case in [tmp+1, tmp-1, tmp*2, tmp-10]:
            # 범위 안에 들어오고 방문한 적이 없는 케이스라면
            if 0 <= case <= 1000000 and not values[case]:
                # 연산 횟수 1씩 증가
                values[case] = values[tmp] + 1
                Q.append(case)


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    # 연산의 범위가 백만 이하의 자연수이므로 1000000까지 인덱스를 가지는 values 리스트 정의
    values = [0] * 1000001
    calc(N)
    # N부터 연산횟수를 1로 설정해놔서
    ans = values[M] -1

    print('#{} {}'.format(t, ans))