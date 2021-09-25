def bfs(s, V): # 인접행렬 방식
    q = []                      # 큐 생성
    visited = [0] * (V+1)         # visited 생성
    q.append(s)                 # 시작점 인큐
    visited[s] = 1              # 시작점 visited 표시
    while q:                    # 큐가 비어있지 않으면(처리할 정점이 남아있지 않으면)
        t = q.pop(0)            # 디큐 (꺼내서)해서 t에 저장
        print(t)                # t에 대한 처리
        # if t == 찾고자 하는 것이면 출력하도록 하면 찾고자 하는 값이 있는지 확인 가능
        for i in range(1, V+1): # t에 인접이고 미방문인 모든 i에 대해
            if adj[t][i] == 1 and visited[i] == 0:
                q.append(i)     # enqueue(i)
                visited[i] = visited[t] + 1     # i visited로 표시

def bfs2(s, V): # 인접 리스트 방식
    q = []                      # 큐 생성
    visited = [0] * (V+1)         # visited 생성
    q.append(s)                 # 시작점 인큐
    visited[s] = 1              # 시작점 visited 표시
    while q:                    # 큐가 비어있지 않으면(처리할 정점이 남아있지 않으면)
        t = q.pop(0)            # 디큐 (꺼내서)해서 t에 저장
        print(t)                # t에 대한 처리
        for i in adjList[t]: # t에 인접이고 미방문인 모든 i에 대해
            if visited[i] == 0:
                q.append(i)     # enqueue(i)
                visited[i] = visited[t] + 1     # i visited로 표시

V, E = map(int, input().split())
edge = list(map(int, input().split()))
adj = [[0]*(V+1) for _ in range(V+1)]                 # 인접행렬
adjList = [[] for _ in range(V+1)]

for i in range(E):
    n1, n2 = edge[2*i], edge[2*i+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1                             #방향이 없는 그래프(양방향 그래프)

    adjList[n1].append(n2)
    adjList[n2].append(n1)

bfs(1, V)
bfs2(1, V)