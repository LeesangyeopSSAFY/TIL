def factory(product, cost):
    global ans
    if cost > ans:
        return
    if product == N:
        ans = cost
        return
    for fact in range(N):
        if visited[fact] == 0:
            visited[fact] = 1
            factory(product+1, cost+arr[product][fact])
            visited[fact] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 987654321
    visited = [0]*N
