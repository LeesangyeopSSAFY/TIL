def DFS(curr):
    # 방문 체크
    visited[curr] = True
    print(chr(curr+65), end=" ")

    # 방문하지 않고 인접한 정점으로 이동
    for i in range(V):
        if adj_arr[curr][i] and not visited[i]:
            DFS(i)


V, E = map(int, input().split())

adj_arr = [[0] * V for _ in range(V)] # 인정햅렬
visited = [False] * V # 방문 체크를 위한
for i in range(E):
    st, ed = map(int, input().split())
    adj_arr[st][ed] = 1  #여기서 끝내면 방향성있는 표시
    adj_arr[ed][st] = 1

DFS(0)