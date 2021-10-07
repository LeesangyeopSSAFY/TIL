# 이건 시간초과
# def perm(idx, check: int):
#     global perm_list
#     if idx == N:
#         perm_list += sel
#         return
#
#     for j in range(N):
#         if check & (1<<j):
#             continue
#         sel[idx] = idx_list[j]
#         perm(idx+1, check | (1<<j))
#
#
# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     ans = 987654321
#     idx_list = []
#     for idx in range(N):
#         idx_list.append(idx)
#     sel = [0] * N
#     perm_list = []
#     perm(0, 0)
#     for i in range(0, len(perm_list), N):
#         cost = 0
#         for j in range(i, i+N):
#             cost += arr[j%N][perm_list[j]]
#         if cost < ans:
#             ans = cost
#
#     print('#{} {}'.format(t, ans))

def min_cost(product, cost):
    global ans
    # 비용이 클 때는 가지치기
    if cost > ans:
        return
    # 제품 다 생산했을 때
    if product == N:
        ans = cost
        return
    for factory in range(N):
        if visited[factory] == 0:
            visited[factory] = 1
            min_cost(product+1, cost+arr[product][factory])
            visited[factory] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 987654321
    visited = [0]*N
    min_cost(0, 0)
    print('#{} {}'.format(t, ans))