# def perm(n, k):
#     if k == n:
#         print(p)
#         return
#     else:
#         for i in range(k, n):
#             p[k], p[i] = p[i], p[k]
#             perm(n, k+1)
#             p[k], p[i] = p[i], p[k]

# p = [1, 2, 3]
# perm(3, 0)
########################순열 2

def f(n, m, k): # n: 순열의 길이, k 결정할 위치
    if n == k:
        print(p)
    else:
        for i in range(m): # 사용할 숫자의 개수만큼
            if u[i]==0:
                u[i] = 1
                p[k] = arr[i]
                f(n, m, k+1)
                u[i] = 0

p = [0]*3
arr = [1, 2, 3, 4, 5]
u = [0]*5
f(3, 5, 0)