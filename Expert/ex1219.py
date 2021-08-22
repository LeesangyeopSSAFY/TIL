def DFS(curr):
    visited[curr] = True

    for i in range(100):
        if adj_arr[curr][i] and not visited[i]:
            DFS(i)

for t in range(1):
    tc_num, road_len = map(int, input().split())
    adj_arr = [[0] * 100 for _ in range(100)]
    visited = [False] * 100
    sted = list(map(int, input().split()))
    for i in range(0, len(sted)-1, 2):
        adj_arr[sted[i]][sted[i+1]] = 1

    DFS(0)
    # if visited[99]:
    #     print("#{} 1".format(tc_num))
    # else:
    #     print("#{} 0".format(tc_num))
    print(visited)