# 중위 순회로 값이 커지므로
def in_order(n):
    if n <= N: # n의 값이 N보다 같거나 작으면
        in_order(n*2)
        arr[n] += max(arr) + 1 # 1씩 증가하게 하기 위해
        in_order(n*2+1)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [0] * (N+1)
    in_order(1)
    print('#{} {} {}'.format(t, arr[1], arr[N//2]))