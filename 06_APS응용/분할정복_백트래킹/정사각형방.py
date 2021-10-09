dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def Link(r, c):
    # 상하좌우 탐색
    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]

        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        # 1 증가하는 방이라면
        if rooms[nr][nc] - rooms[r][c] == 1:
            link_list[rooms[nr][nc]] += 1
            Link(nr, nc)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    # link_list: 연결된 방의 갯수 체크
    link_list = [0] + [1]*(N**2)
    for r in range(N):
        for c in range(N):
            Link(r, c)

    max_val = 0
    max_idx = 0
    # 뒤에서부터 돌면서
    for idx in range(len(link_list)-1, 0, -1):
        # >=를 이용하여 큰 값 중에 가장 작은 인덱스 구하기
        if link_list[idx] >= max_val:
            max_val = link_list[idx]
            max_idx = idx
    print('#{} {} {}'.format(t, max_idx-max_val+1, max_val))