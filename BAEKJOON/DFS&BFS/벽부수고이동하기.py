import copy, sys
from collections import deque
input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def bfs():
    Q = deque()
    Q.append([0, 0, 1])
    visited = [[[0]*2 for i in range(M)] for i in range(N)]
    visited[0][0][1] = 1
    while Q:
        r, c, w = Q.popleft()
        if r == N-1 and c == M-1:
            return visited[r][c][w]
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if 0<=nr<N and 0<=nc<M:
                if zido[nr][nc] == 1 and w == 1:
                    visited[nr][nc][0] = visited[r][c][1] + 1
                    Q.append([nr, nc, 0])
                elif zido[nr][nc] == 0 and visited[nr][nc][w] == 0:
                    visited[nr][nc][w] = visited[r][c][w] + 1
                    Q.append([nr, nc, w])
    return -1


N, M = map(int, input().split())
zido = []
for _ in range(N):
    zido.append(list(map(int, list(input().strip()))))
print(bfs())
# def bfs(each_zido):
#     global ans
#     Q = deque()
#     Q.append((0, 0))
#     each_zido[0][0] = 1
#     while Q:
#         r, c = Q.popleft()
#         for dir in range(4):
#             nr = r + dr[dir]
#             nc = c + dc[dir]
#             if 0<=nr<N and 0<=nc<M:
#                 if each_zido[nr][nc] == '0':
#                     each_zido[nr][nc] = each_zido[r][c] + 1
#                     Q.append((nr, nc))
    
#     if each_zido[N-1][M-1] != '0' and each_zido[N-1][M-1] < ans:
#         ans = each_zido[N-1][M-1]



# N, M = map(int, input().split())
# zido = []
# for _ in range(N):
#     zido.append(list(map(str, input())))

# ans = 987654321
# bfs(zido)
# for i in range(N):
#     for j in range(M):
#         if zido[i][j] == '1':
#             tmp_zido = copy.deepcopy(zido)
#             tmp_zido[i][j] = '0'
#             bfs(tmp_zido)

# if ans == 987654321:
#     print(-1)
# else:
#     print(ans)
