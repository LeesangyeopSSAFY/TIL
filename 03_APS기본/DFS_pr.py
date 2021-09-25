def DFS(st):
    stack = []
    stack.append(st) # 시작점 추가

    while stack:
        curr = stack.pop() # stack에서 하나 꺼낸 후
        if not visited[curr]: # 방문하지 않은 지점이라면.
            visited[curr] = True
            #####할 일######
            
            for i in range(V): # 노드의 수만큼 반복문을 돌면서
                if adj_arr[curr][i] and not visited[i]: # 연결되어 있고 방문하지 않았다면
                    stack.append(i) # 스택에 추가


V, E = map(int, input().split())

adj_arr = [[0]*V for _ in range(V)]
visited = [False] * V
for i in range(E):
    st, ed = map(int, input().split())
    adj_arr[st][ed] = 1
    adj_arr[ed][st] = 1 # 방향성이 없는 경우 이 라인이 필요, 방향성이 있으면 노 필요

DFS(0)