# 딱지 놀이
def battle():
    if A[4] != B[4]:
        if A[4] < B[4]:
            return 'B'
    elif A[4] == B[4] and A[3] != B[3]:
        if A[3] < B[3]:
            return 'B'
    elif A[4] == B[4] and A[3] == B[3] and A[2] != B[2]:
        if A[2] < B[2]:
            return 'B'
    elif A[4] == B[4] and A[3] == B[3] and A[2] == B[2] and A[1] != B[1]:
        if A[1] < B[1]:
            return 'B'
    elif A[4] == B[4] and A[3] == B[3] and A[2] == B[2] and A[1] == B[1]:
        return 'D'
    return 'A'

N = int(input())
for n in range(N):
    A = [0] * 5
    B = [0] * 5
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(1, len(a)):
        A[a[i]] += 1
    for j in range(1, len(b)):
        B[b[j]] += 1

    winner = battle()
    print(winner)