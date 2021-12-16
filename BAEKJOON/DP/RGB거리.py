import sys
input = sys.stdin.readline


N = int(input())
R, G, B = 0, 1, 2
cost_list = []
for _ in range(N):
    cost_list.append(list(map(int, input().split())))

dp = [[0]*3 for _ in range(N)]
dp[0][R], dp[0][G], dp[0][B] = cost_list[0][R], cost_list[0][G], cost_list[0][B]

for i in range(1, N):
    dp[i][R] = min(dp[i-1][G], dp[i-1][B]) + cost_list[i][R]
    dp[i][G] = min(dp[i-1][R], dp[i-1][B]) + cost_list[i][G]
    dp[i][B] = min(dp[i-1][R], dp[i-1][G]) + cost_list[i][B]

print(min(dp[N-1]))



# def RGB(last_color, idx, cost):
#     global ans
#     if idx == N and cost < ans:
#         ans = cost
#         return
#     if cost >= ans: return
#     mini = 1000
#     min_idx = 0
#     for color in range(3):
#         if color != last_color:
#             if cost_list[idx][color] < mini:
#                 mini = cost_list[idx][color]
#                 min_idx = color
#     RGB(min_idx, idx+1, cost + mini)

# N = int(input())
# cost_list = []
# for _ in range(N):
#     cost_list.append(list(map(int, input().split())))
# ans = 987654321
# for i in range(3):
#     RGB(i, 1, cost_list[0][i])
# print(ans)