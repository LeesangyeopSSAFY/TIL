def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)


N = int(input())
# ans = fibo(N)
# print(ans)
# memo = [0, 1]
#
# def fibo1(n):
#     global memo
#     if n >= 2 and len(memo) <= n:
#         memo.append(fibo1(n-1) + fibo1(n-2))
#     return memo[n]
#
# print(fibo1(N))

def fibo2(n):
    f = [0, 1]

    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])

    return f[n]

print(fibo2(N))