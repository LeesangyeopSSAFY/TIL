def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())

    edges = [list(map(int, input().split())) for _ in range(E)]
    # 가중치를 기준으로 오름차순 정렬
    edges.sort(key=lambda x: x[2])

    p = [0] * (V+1)
    for i in range(V+1):
        make_set(i)
    
    ans = 0

    pick = 0
    idx = 0
    # 간선의 개수는 정점수 -1개
    while pick < V:
        x = edges[idx][0]
        y = edges[idx][1]

        # x와 y의 대표 정점이 다르면
        if find_set(x) != find_set(y):
            union(x, y)
            pick += 1
            ans += edges[idx][2]

        idx += 1
    
    print('#{} {}'.format(t, ans))