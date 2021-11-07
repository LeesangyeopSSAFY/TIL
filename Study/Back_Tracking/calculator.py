def calc(n, total, pl, mi, mu, di):
    global maxi, mini
    if n == N:
        maxi = max(total, maxi)
        mini = min(total, mini)
        return

    if pl:
        calc(n+1, total + nums[n], pl-1, mi, mu, di)
    if mi:
        calc(n+1, total - nums[n], pl, mi-1, mu, di)
    if mu:
        calc(n+1, total * nums[n], pl, mi, mu-1, di)
    if di:
        calc(n+1, int(total / nums[n]), pl, mi, mu, di-1)

N = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))

maxi = -1000000000
mini = 1000000000

calc(1, nums[0], oper[0], oper[1], oper[2], oper[3])
print(maxi)
print(mini)