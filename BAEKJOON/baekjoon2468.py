from collections import deque
import sys
import copy
input = sys.stdin.readline

#### 80% 쯤에서 에러 발생...####

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    visited[x][y] = 1
    while Q:
        r, c = Q.popleft()
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if zido[nr][nc] > 0 and visited[nr][nc] == 0:
                Q.append((nr, nc))
                visited[nr][nc] = 1

maxi = 0
N = int(input())
region = []
for n in range(N):
    line = list(map(int, input().split()))
    # 들어온 입력 중에 가장 큰 수 구하기
    if max(line) > maxi:
        maxi = max(line)
    region.append(line)

ans_list = []
for height in range(1, maxi+1):
    # 차오르는 높이마다 비교해야 하므로 deepcopy
    zido = copy.deepcopy(region)
    for r in range(N):
        for c in range(N):
            if zido[r][c] <= height:
                zido[r][c] = 0
    
    cnt = 0
    visited = [[0]*N for _ in range(N)]
    for r1 in range(N):
        for c1 in range(N):
            if zido[r1][c1] > 0 and visited[r1][c1] == 0:
                bfs(r1, c1)
                cnt += 1
    ans_list.append(cnt)

print(max(ans_list))