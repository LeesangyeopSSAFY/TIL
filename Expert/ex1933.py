# 간단한 N의 약수
N = int(input())
lists = []
for n in range(1, N+1):
    if N % n == 0: # N을 n으로 나눈 나머지가 0이면
        print(n, end=' ')