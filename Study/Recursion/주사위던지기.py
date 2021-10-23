# def type1(idx):
#     if idx == N:
#         for n in range(N):
#             if n == N-1:
#                 print(ans_list[n])
#             else:
#                 print(ans_list[n], end=' ')
#         return
#     for i in range(1, 7):
#         ans_list[idx] = i
#         type1(idx+1)
#
# def type2(idx):
#     if idx == N:
#         tmp = sorted(ans_list)
#         if tmp in double_check:
#             return
#         double_check.append(tmp)
#         for n in range(N):
#             if n == N-1:
#                 print(ans_list[n])
#             else:
#                 print(ans_list[n], end=' ')
#         return
#
#     for i in range(1, 7):
#         ans_list[idx] = i
#         type2(idx+1)
#
#
# def type3(idx):
#     if idx == N:
#
#         for n in range(N):
#             if n == N-1:
#                 print(ans_list[n])
#             else:
#                 print(ans_list[n], end=' ')
#         return
#
#     for i in range(1, 7):
#         if used[i] == 1:
#             continue
#         used[i] = 1
#         ans_list[idx] = i
#         type3(idx+1)
#         used[i] = 0
#
# N, M = map(int, input().split())
# ans_list = [0 for _ in range(N)]
# used = [0 for _ in range(7)]
# double_check = []
# if M == 1:
#     type1(0)
# elif M == 2:
#     type2(0)
# elif M == 3:
#     type3(0)

####################################################
from itertools import combinations, permutations

print(list(combinations([1, 2, 3, 4, 5], 2)))
print(list(permutations([1, 2, 3, 4, 5], 2)))
