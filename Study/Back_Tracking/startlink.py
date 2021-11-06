from itertools import combinations

def startlink(A):
    total = 0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            total += arr[A[i]][A[j]]
            total += arr[A[j]][A[i]]

    return total

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
half = N // 2

idx_arr = [i for i in range(N)]
comb = list(combinations(idx_arr, half))
ans = 987654321
for i in range(len(comb)//2):
    tmp1 = startlink(comb[i])
    tmp2 = startlink(comb[len(comb)-1-i])
    tmp = abs(tmp1 - tmp2)
    if tmp == 0:
        ans = 0
        break
    elif tmp < ans:
        ans = tmp

print(ans)
