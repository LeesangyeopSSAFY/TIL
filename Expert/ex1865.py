# 동철이의 일 분배
def schedule(n, val, visited):
    global ans
    if val <= ans or val == 0:
        return
    if n == N and val > ans:
        ans = val
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            n_val = val * P_list[n][i] / 100
            schedule(n+1, n_val, visited)
            visited[i] = 0



T = int(input())
for t in range(1, T+1):
    P_list = []
    N = int(input())
    for _ in range(N):
        tmp = list(map(int, input().split()))
        P_list.append(tmp)

    ans = 0
    for i in range(N):
        visited = [0] * N
        visited[i] = 1
        schedule(1, P_list[0][i]/100, visited)
    
    ans *= 100
    print(f'#{t} {ans:.6f}')