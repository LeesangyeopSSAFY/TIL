import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
adj_list = [[]*(V+1) for _ in range(V+1)]
val_arr = [[0]*(V+1) for _ in range(V+1)]
for e in range(E):
    u, v, w = map(int, input().split())
    adj_list[u].append(v)
Q = []
visited = [-1] * (V+1)
visited[K] = 0
Q.append(K)
while Q:
    t = Q.pop(0)
    for i in adj_list[t]:
        for j in range(1, V+1) 
### 모르겠습니다...