def Prim():
    dist = [987654321] * (V+1)
    visited = [0] * (V+1)

    dist[0] = 0

    for _ in range(V):
        min_idx = -1
        min_val = 987654321

        for i in range(V+1):
            if not visited[i] and dist[i] < min_val:
                min_idx = i
                min_val = dist[i]
        
        visited[min_idx] = True

        for i in range(V+1):
            if not visited[i] and adj_arr[min_idx][i] < dist[i]:
                dist[i] = adj_arr[min_idx][i]
    
    return sum(dist)


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())

    adj_arr = [[987654321] * (V+1) for _ in range(V+1)]

    for i in range(E):
        n1, n2, w = map(int, input().split())
        adj_arr[n1][n2] = w
        adj_arr[n2][n1] = w
    
    print('#{} {}'.format(t, Prim()))