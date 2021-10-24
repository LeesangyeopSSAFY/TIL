# idx: 현재 내가 있는 버스 정류장 번호
# e: 잔여 배터리
# c: 교환 횟수

def move(idx, e, c):
    global ans
    if idx == bus_stop[0]:
        if ans > c: # 만약 교환 횟수가 더 작다면
            ans = c
        else:
            # 배터리를 교체하지 않고 내려보내기
            if e > 0:
                move(idx+1, e-1, c)
            # 배터리 교체하고 내려보내기
            if c < ans:
                move(idx+1, bus_stop[idx]-1, c+1)


T = int(input())
for t in range(1, T+1):
    bus_stop = list(map(int, input().split()))

    ans = 987654312
    # 정류장이 1번 인덱스부터 시작하고 처음 정류장은 카운트에서 제외하므로 카운트는 0, 다음 칸으로 이동하기 위해서 1번 인덱스 값에서 1빼주기
    move(2, bus_stop[1]-1, 0)

    print('#{} {}'.format(t, ans))

