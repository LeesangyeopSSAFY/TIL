# 최대 상금
# def find_max(N):
#     global c
#     double = []
#     for i in range(len(N)):
#         for j in range(len(N)-1, i-1, -1):
#             if N[i] < N[j] and N[j] == max(N[i+1:]):
#                 N[i], N[j] = N[j], N[i]
#                 c += 1
#             elif N[i] == N[j] and not double: 
#                 double = [i, j]
#             if c == C:
#                 return
#             elif N == max_N:
#                 return double

# T = int(input())
# for t in range(1, T+1):
#     N1, C = input().split()
#     N = []
#     for n in N1:
#         N.append(int(n))
#     C = int(C)
#     tmp_N = sorted(N)
#     max_N = reversed(tmp_N)
#     c = 0
#     double = find_max(N)
#     if c != C:
#         while c != C:
#             if double:
#                 N[double[0]], N[double[1]] = N[double[1]], N[double[0]]
#             else:
#                 N[-2], N[-1] = N[-1], N[-2]
#             c += 1
#     ans = 0
#     for n in range(len(N)):
#         ans += N[n] * 10**(len(N)-n-1)
#     print('#{} {}'.format(t, ans))


def find_max(idx, c):
    global ans
    # 교환 횟수를 다 쓰면
    if c == C:
        # 비교 후 큰 값을 ans에 저장
        ans = max(int(''.join(N)), ans)
        return
    for i in range(idx, len(N)):
        for j in range(i+1, len(N)):
            # 뒤쪽 인덱스의 값이 크거나 같으면 바꿔주고 재귀
            if N[i] <= N[j]:
                N[i], N[j] = N[j], N[i]
                find_max(i, c+1)
                # 다시 N 복구
                N[i], N[j] = N[j], N[i]
    # 다 정렬을 했는데도 교환 횟수를 못 채웠다면
    if not ans:
        N[-2], N[-1] = N[-1], N[-2]
        find_max(idx, c+1)


T = int(input())
for t in range(1, T+1):
    N, C = input().split()
    C = int(C)
    N = list(N)
    ans = 0
    find_max(0, 0)
    print('#{} {}'.format(t, ans))