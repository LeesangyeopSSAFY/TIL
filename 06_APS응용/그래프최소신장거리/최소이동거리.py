def fastest():
    Q = [0]
    # 0번부터 시작하므로 0번 거리를 0으로
    distance[0] = 0
    while Q:
        curr = Q.pop(0)
        # 0부터 인접 리스트를 순회하면서
        for check, multi in adjList[curr]:
            # 제일 최소 이동 거리를 계산
            if distance[check] > distance[curr] + multi:
                distance[check] = distance[curr] + multi
                Q.append(check)



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # V: 마지막 정점의 번호, E: 간선의 개수
    distance = [987654321] * (V+1)
    adjList = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2, w = map(int, input().split())
        # 인접 리스트에 인접 정점과 가중치를 가진 리스트 추가
        adjList[n1].append([n2, w])

    fastest()
    ans = distance[V]
    print('#{} {}'.format(tc, ans))