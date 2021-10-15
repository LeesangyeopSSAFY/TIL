from collections import deque

# idx에서 X번 집으로 가는 동안 걸리는 시간
def go(idx):
    dist = [987654321] * (N+1)
    Q = deque()
    Q.append(idx)
    dist[idx] = 0
    while Q:
        curr = Q.popleft()
        for dest, time in adjList[curr]:
            # 만약 기존 시간보다 더 빨리 갈 수 있는 경우라면
            if dist[dest] > dist[curr] + time:
                dist[dest] = dist[curr] + time
                Q.append(dest)

    return dist[X]

# X번 집에서 idx번 집으로 돌아오는 시간
def come(idx):
    dist = [987654321] * (N + 1)
    Q = deque()
    Q.append(X)
    dist[X] = 0
    while Q:
        curr = Q.popleft()
        for dest, time in adjList[curr]:
            if dist[dest] > dist[curr] + time:
                dist[dest] = dist[curr] + time
                Q.append(dest)
    return dist[idx]

T = int(input())
for t in range(1, T+1):
    N, M, X = map(int, input().split())
    adjList = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        # 인접 리스트에 도착 집(y)와 시간을 리스트로 만들어서 추가
        adjList[x].append([y, c])

    # ans_lsit: 각 집 별로 X번 집으로 오고 가는데 드는 시간을 저장하는 리스트
    ans_list = [0] * (N+1)

    for i in range(1, N+1):
        if i != X:
            ans_list[i] += go(i)
            ans_list[i] += come(i)

    print('#{} {}'.format(t, max(ans_list)))