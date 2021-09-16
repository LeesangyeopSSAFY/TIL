import sys
input = sys.stdin.readline
# 반복의 기본값이 1000회 이므로 늘려줘야한다.
sys.setrecursionlimit(10**9)

def dfs(st):
    for i in tree[st]:
        if par[i] == 0:
            par[i] = st
            dfs(i)


N = int(input())
tree = [[] for _ in range(N+1)]

par = [0 for _ in range(N+1)]

for n in range(N-1):
    a, b = list(map(int, input().split()))
    tree[a].append(b)
    tree[b].append(a)

dfs(1)

for i in range(2, N+1):
    print(par[i])
