def bfs(s):
    q = []
    visited = [0] * (V+1)
    q.append(s)
    visited[s] = 1
    cnt = -1 # cnt를 -1로 준 것은 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터 수이므로 체크하지 않는다.
    while q:
        t = q.pop(0)
        cnt += 1
        for i in adjList[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1
    return cnt


V = int(input())
E = int(input())
adjList = [[] for _ in range(V+1)]

for i in range(E):
    n1, n2 = map(int, input().split())
    adjList[n1].append(n2)
    adjList[n2].append(n1)

print(bfs(1)) # 1번 컴퓨터부터 시작