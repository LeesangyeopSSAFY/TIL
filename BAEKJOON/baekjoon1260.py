def dfs(V):
    print(V, end=' ')
    visited[V] = 1
    for i in range(1, N+1):
        if visited[i] == 0 and ad[V][i] == 1:
            dfs(i)

def bfs(V):
    q = [V]
    visited[V] = 0 # dfs를 통해 이미 1이 되었으니 0으로 바꿔준다.
    while q:
        v = q.pop(0)
        print(v, end=' ')
        for j in range(1, N+1):
            if visited[j] == 1 and ad[v][j] == 1:
                q.append(j)
                visited[j] = 0


N, M, V = map(int, input().split())
ad = [[0]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    n1, n2 = map(int, input().split())
    ad[n1][n2] = 1
    ad[n2][n1] = 1

dfs(V)
print()
bfs(V)