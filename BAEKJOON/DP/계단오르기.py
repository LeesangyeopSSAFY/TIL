# 재귀로 하면 시간초과 발생
# def steps(idx, dup, val):
#     global ans
#     if idx >= N:
#         if val + stairs[N] > ans:
#             ans = val + stairs[N]
#             return
#     elif dup == 0:
#         steps(idx+1, 2, val)
#         return
#     else:
#         steps(idx+1, dup-1, val+stairs[idx])
#         steps(idx+2, 2, val+stairs[idx])
import sys
input = sys.stdin.readline

N = int(input())
stairs = [0]
for _ in range(N):
    stairs.append(int(input()))

if N == 1:
    print(stairs[1])
else:
    sum_list = [0] * (N+1)
    sum_list[1] = stairs[1]
    sum_list[2] = stairs[1] + stairs[2]

    for idx in range(3, N+1):
        sum_list[idx] = max(sum_list[idx-3]+stairs[idx-1]+stairs[idx], sum_list[idx-2]+stairs[idx])

    print(sum_list[N])
