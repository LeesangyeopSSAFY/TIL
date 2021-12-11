from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# def bfs(r, c, cnt, done):
#     global ans
#     if r == N-1 and c == M-1:
#         if cnt < ans:
#             ans = cnt
#             return cnt
#     if cnt > ans: return
#     for dir in range(4):
#         nr = r + dr[dir]
#         nc = c + dc[dir]
#         if 0<=nr<N and 0<=nc<M:
#             if maze[nr][nc] == '1' and not done[nr][nc]:
#                 done[nr][nc] = 1
#                 bfs(nr, nc, cnt+1, done)
#                 done[nr][nc] = 0

def bfs2():
    Q = deque()
    Q.append((0, 0))
    while Q:
        r, c = Q.popleft()
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if 0<=nr<N and 0<=nc<M:
                if maze2[nr][nc] == '1':
                    Q.append((nr, nc))
                    maze2[nr][nc] = maze2[r][c] + 1 


N, M = map(int, input().split())
# maze = []
maze2 = []
for n in range(N):
    # maze.append(tmp)
    maze2.append(list(input()))
# visited = [[False]*M for _ in range(N)]
maze2[0][0] = 1
# ans = 987654321
# visited[0][0] = 1
# bfs(0, 0, 1, visited)
# print(ans)
bfs2()
print(maze2[N-1][M-1])