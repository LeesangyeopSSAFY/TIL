def type1(n):
    if n == N:
        print(*arr)
        return
    for i in range(1, 7):
        arr[n] = i
        type1(n+1)

def type2(idx, val):
    if idx == N:
        print(*arr)
        return
    
    for v in range(val, 7):
        arr[idx] = v
        type2(idx+1, v)

def type3(n):
    if n == N:
        print(*arr)
        return
    for i in range(1, 7):
        if not visited[i]:
            visited[i] = 1
            arr[n] = i
            type3(n+1)
            visited[i] = 0


# N: 고르는 횟수, M: 타입
N, M = map(int, input().split())
arr = [0] * N
visited = [0]*7

if M == 1:
    type1(0)
elif M == 2:
    type2(0, 1)
elif M == 3:
    type3(0)