def DFS(curr):
    # 방문 체크
    visited[curr] = True

    # 방문하지 않고 인접한 정점으로 이동
    for i in range(V+1):
        if adj_arr[curr][i] and not visited[i]:
            DFS(i)

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split()) #노드와 간선
    adj_arr = [[0] * (V+1) for _ in range(V+1)] #인접 행렬
    visited = [False] * (V+1) # 방문 체크용
    for e in range(E):
        st, ed = map(int, input().split())
        adj_arr[st][ed] = 1 # 방향성이 있는 표시

    sigak, kkeut = map(int, input().split())

    DFS(sigak)
    # visted의 끝 정점이 True라면 1출력
    if visited[kkeut]:
        print("#{} 1".format(t))
    else:
        print("#{} 0".format(t))