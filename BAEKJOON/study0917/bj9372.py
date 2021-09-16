import sys
input = sys.stdin.readline

def dfs(st, cnt):
    visited[st] = 1

    for i in tree[st]:
        if visited[i] == 0:
            cnt = dfs(i, cnt+1)
    
    return cnt


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    tree = [[] for _ in range(N+1)]
    for m in range(M):
        a, b = list(map(int, input().split()))
        tree[a].append(b)
        tree[b].append(a)

    visited = [0]*(N+1)

    print(dfs(1, 0))

