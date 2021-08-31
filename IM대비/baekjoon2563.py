# 색종이
N = int(input())
dohwaji = [[0]*100 for _ in range(100)]
for n in range(N):
    r, c = map(int, input().split())
    for i in range(10):
        for j in range(10):
            dohwaji[r+i][c+j] += 1

more = 0
for a in range(100):
    for b in range(100):
        if dohwaji[a][b] > 1:
            more += (dohwaji[a][b] - 1) # 중복되서 겹칠 경우에는 중복된 수만큼 빼줘야 한다.

ans = N*100 - more
print(ans)