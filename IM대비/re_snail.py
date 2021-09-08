N = int(input())
box = []
for n in range(N):
    box.append([0]*N)

dr = [0, 1, 0, -1] # 우 하 좌 상
dc = [1, 0, -1, 0]
value = 1
r, c = 0, -1 #c가 -1부터인 이유는 nr, nc로 인해서 처음이 (0, 0)이 되도록 하기 위해
dir = 0

while value <= N*N:
    nr = r + dr[dir]
    nc = c + dc[dir]
    if 0 <= nr < N and 0 <= nc < N and box[nr][nc] == 0: #nr, nc가 상자 범위 안이고 값이 없다면
        box[nr][nc] == value
        value += 1 # value 하나 증가
        r, c = nr, nc # 좌표 값 갱신
    else:
        dir = (dir+1) % 4

print(box)