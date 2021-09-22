def fib(n):
    # base case
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

# 반복문 사용
def fibo_for(n):
    if n < 2:
        return n

    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a+b
    return b #a+b값이 계속 뒤쪽으로 가니까 마지막 답이 b에 반환된다.

print(fibo_for(4))
