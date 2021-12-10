from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    global ans
    Q = deque()
    Q.append((0, 0))
    visited[0][0] = True
    while Q:
        r, c = Q.popleft()
        ans += 1
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if nr == N-1 and nc == M-1:
                return ans
            if 0 <= nr < N and 0<= nc < M:
                if maze[nr][nc] == '1' and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    Q.append((nr, nc))


N, M = map(int, input().split())
maze = []
for n in range(N):
    tmp = input()
    maze.append(tmp)
visited = [[False]*M for _ in range(N)]
ans = 0
bfs()
print(ans)