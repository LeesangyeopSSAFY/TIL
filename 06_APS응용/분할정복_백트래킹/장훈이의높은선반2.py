def make_tower(n, height):
    global ans, flag

    if flag:
        return
    if height >= B:
        if height == B:
            flag = 1
        ans = height
        return
    
    for i in range(n, N):
        if not visited[i] and height + tc[i] < ans:
            visited[i] = 1
            make_tower(i, height + tc[i])
            visited[i] = 0


T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    tc = sorted(list(map(int, input().split())), reverse=True)
    visited = [0] * N
    ans = 987654321
    flag = 0
    make_tower(0, 0)

    print('#{} {}'.format(t, ans-B))