def best(worker, percent):
    global ans
    # percent가 ans보다 작아지는 순간 더 커질 수는 없으므로 바로 리턴
    if percent <= ans:
        return
    if worker == N:
        ans = percent
        return
    for work in range(N):
        if visited[work] == 0:
            visited[work] = 1
            best(worker+1, percent*arr[worker][work]/100)
            visited[work] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    ans = 0
    best(0, 1)
    ans = ans * 100
    print('#{} {:.6f}'.format(t, ans))