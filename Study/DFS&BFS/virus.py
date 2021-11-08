def dfs(st):
    cnt = 0
    visited = [0] * (v+1)
    stack = []
    stack.append(st)
    visited[st] = 1

    while stack:
        curr = stack.pop()

        for i in adj_list[curr]:
            if not visited[i]:
                cnt += 1
                visited[i] = 1
                stack.append(i)
    return cnt


v = int(input()) # 노드
e = int(input())

adj_list = [[] for _ in range(v+1)]

for i in range(e):
    st, ed = map(int,input().split())
    adj_list[st].append(ed)
    adj_list[ed].append(st)

print(dfs(1))

##############################
# bfs
from collections import deque

def bfs(idx):
    Q = deque()
    Q.append(idx)
    visited[idx] = True
    cnt = 0
    while Q:
        tmp = Q.popleft()
        cnt += 1
        for i in adjList[tmp]:
            if not visited[i]:
                visited[i] = True
                Q.append(i)
    return cnt



V = int(input())
E = int(input())
adjList = [[] for _ in range(V+1)]
for _ in range(E):
    n1, n2 = map(int, input().split())
    adjList[n1].append(n2)
    adjList[n2].append(n1)

visited = [False] * (V+1)
print(bfs(1)-1)