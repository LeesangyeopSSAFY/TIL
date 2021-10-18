def tour(r, c, left, right):
    global ans
    cafe = [0] * 101
    cnt = 0 # 지나간 카페 수
    # 왼쪽 꼭지점
    lr = r + left
    lc = c - left
    # 아래 꼭지점
    br = r + left + right
    bc = c - left + right
    # 오른쪽 꼭지점
    rr = r + right
    rc = c + right

    for dis in range(1, left+1):
        # 만약 이미 들렀던 카페라면
        if cafe[cafes[r+dis][c-dis]]:
            return
        # 시작점에서 부터 왼쪽으로 내려올 때
        cafe[cafes[r+dis][c-dis]] = 1
        if cafe[cafes[br-dis][bc+dis]]:
            return
        # 바닥점에서 오른쪽 꼭지점까지 올라갈 때
        cafe[cafes[br - dis][bc + dis]] = 1
        cnt += 2

    for dis in range(1, right+1):
        if cafe[cafes[lr+dis][lc+dis]]:
            return
        # 왼쪽 꼭지점에서 바닥점까지 내려갈 때
        cafe[cafes[lr + dis][lc + dis]] = 1
        if cafe[cafes[rr-dis][rc-dis]]:
            return
        # 오른쪽 꼭지점에서 원래 시작점으로 돌아갈 때
        cafe[cafes[rr - dis][rc - dis]] = 1
        cnt += 2
    # 가장 먼 길 고르기
    ans = max(ans, cnt)

# where_to_go: 시작점으로 좌, 우 가능한 거리의 경우 구하는 함수
def where_to_go(r, c):
    for left in range(1, c+1):
        for right in range(1, N-c):
            # 범위 넘어가면 패스
            if r + left + right > N-1:
                continue
            tour(r, c, left, right)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    # 행은 끝에서 두번째 행 까지
    for r in range(N-2):
        # 열은 1번째부터 N-2까지만 대각선으로 이동 가능하므로
        for c in range(1, N-1):
            where_to_go(r, c)

    print('#{} {}'.format(t, ans))