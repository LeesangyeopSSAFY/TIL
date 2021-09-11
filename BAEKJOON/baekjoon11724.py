# 연결 요소의 개수
from collections import deque
import sys
input = sys.stdin.readline

def bfs(s, N):
    q = deque([s])
    visited[s] = True
    while q:
        v = q.popleft()
        for i in adj_list[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


N, M = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for m in range(M):
    n1, n2 = map(int, input().split())
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

ans = 0
for i in range(1, N+1):
    if not visited[i]:
        bfs(i, N)
        ans += 1

print(ans)
