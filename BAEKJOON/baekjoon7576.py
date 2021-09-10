# 토마토
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def bfs():
    while Q:
        curr_r, curr_c = Q.pop(0)
        for dir in range(4):
            nr = curr_r + dr[dir]
            nc = curr_c + dc[dir]

            if 0<= nr < N and 0<= nc < M and box[nr][nc] == 0: # 범위 확인 및 익지 않은 토마토라면
                Q.append((nr, nc))
                box[nr][nc] = box[curr_r][curr_c] + 1


M, N = map(int, input().strip().split())
box = []
for _ in range(N):
    box.append(list(map(int, input().split())))

Q = []
# 반복문 돌면서 익은 토마토 확인 후 Q에 추가
for n in range(N):
    for m in range(M):
        if box[n][m] == 1:
            Q.append((n, m))

bfs()

maxi = -987654321
cnt_0 = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 0: # 익지 않은 토마토가 하나라도 있는 경우
            cnt_0 += 1
            break
        elif box[i][j] > maxi: # 가장 큰 수(날짜)
            maxi = box[i][j]
    if cnt_0 > 0:
        break

if cnt_0 > 0:
    print(-1)
else:
    print(maxi-1)

