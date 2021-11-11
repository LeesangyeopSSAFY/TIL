from collections import deque

def dfs(idx):
    cnt = 0
    visited = [0] * (V+1)
    stack = [idx]
    visited[idx] = 1
    while stack:
        curr = stack.pop()
        for i in adjList[curr]:
            if not visited[i]:
                visited[i] = 1
                cnt += 1
                stack.append(i)
    
    return cnt

def DFS(idx):
    global ans
    visited[idx] = 1
    for i in adjList[idx]:
        if not visited[i]:
            ans += 1
            DFS(i)

def bfs(idx):
    cnt = 0
    visited = [0] * (V+1)
    Q = deque()
    Q.append(idx)
    visited[idx] = 1
    while Q:
        curr = Q.popleft()
        for i in adjList[curr]:
            if not visited[i]:
                visited[i] = 1
                cnt += 1
                Q.append(i)
    
    return cnt

V = int(input())
E = int(input())
adjList = [[] for _ in range(V+1)]
for _ in range(E):
    n1, n2 = map(int, input().split())
    adjList[n1].append(n2)
    adjList[n2].append(n1)

ans = 0
visited = [0] * (V+1)


DFS(1)
print(ans)