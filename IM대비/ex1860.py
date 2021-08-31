# 진기의 최고급 붕어빵
# 이건 시간 초과
# T = int(input())
# for t in range(1, T+1):
#     N, M, K = map(int, input().split())
#     check = [0] * 11111
#     for i in range(1, len(check)):
#         if i % M == 0:
#             check[i:] = [i//M*K]*len(check[i:])
#
#     people = list(map(int, input().strip().split()))
#     people.sort()
#     ans = 'Possible'
#     for person in people:
#         if check[person] > 0:
#             for j in range(person, len(check)):
#                 check[j] -= 1
#         else:
#             ans = 'Impossible'
#             break
#     print("#{} {}".format(t, ans))

T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    people = list(map(int, input().strip().split()))
    people.sort()
    ans = 'Possible'
    for n in range(N):
        bread = people[n]//M*K
        if n+1 > bread: # 들어온 사람이 만든 빵보다 크다면
            ans = 'Impossible'
            break
    print("#{} {}".format(t, ans))