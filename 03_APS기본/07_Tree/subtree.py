def pre_order(n): # 전위순회
    global cnt
    if n:
        cnt += 1
        pre_order(left[n])
        pre_order(right[n])

T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split())
    V = E+1 # 정점의 개수
    edge = list(map(int, input().split()))
    left = [0]*(V+1)
    right = [0]*(V+1)

    for e in range(E):
        p, c = edge[e*2], edge[e*2+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    cnt = 0
    pre_order(N)
    print('#{} {}'.format(t, cnt))