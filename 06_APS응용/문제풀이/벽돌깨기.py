import copy

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bomb(r, c, cur_bricks):
    Q = [(r, c, cur_bricks[r][c])]
    cur_bricks[r][c] = 0

    bomb_cnt = 1
    while Q:
        curr_r, curr_c, val = Q.pop(0)
        # 각 벽돌의 값만큼 4방향 벽돌 깨기
        for v in range(1, val):
            for dir in range(4):
                nr = curr_r + dr[dir]*v
                nc = curr_c + dc[dir]*v
                if 0<=nr<H and 0<=nc<W and cur_bricks[nr][nc] != 0:
                    # 1보다 큰 값이라면
                    if cur_bricks[nr][nc] != 1:
                        Q.append((nr, nc, cur_bricks[nr][nc]))
                    bomb_cnt += 1
                    # 1일 떄는 그 벽돌만 바꾸면 되므로
                    cur_bricks[nr][nc] = 0
    return bomb_cnt

def gravity(bricks):
    for w in range(W):
        line = []
        for h in range(H-1, -1, -1):
            # 값이 남은 벽돌을
            if bricks[h][w] != 0:
                # line에 모두 집어넣은 후
                line.append(bricks[h][w])
                bricks[h][w] = 0

        for l in range(len(line)):
            # 밑 행부터 다시 쌓아올리기
            bricks[H-1-l][w] = line[l]


def marble(result, n, bricks):
    global maxi
    if n == N:
        if maxi < result:
            maxi = result
        return
    for w in range(W):
        new_bricks = copy.deepcopy(bricks)
        # curr_h는 각 열마다 가장 높은 곳 즉 구슬을 맞을 수 있는 곳을 나타내는 변수
        curr_h = 0
        while curr_h < H and not new_bricks[curr_h][w]:
            curr_h += 1

        # num_bomb: 터지는 벽돌 수 쳌
        num_bomb = 0
        if curr_h < H:
            num_bomb = bomb(curr_h, w, new_bricks)
            gravity(new_bricks)
        marble(result + num_bomb, n+1, new_bricks)


T = int(input())
for t in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    num_of_bricks = 0
    for h in range(H):
        for w in range(W):
            if arr[h][w] != 0:
                num_of_bricks += 1
    maxi = 0
    marble(0, 0, arr)
    ans = num_of_bricks - maxi
    print('#{} {}'.format(t, ans))
