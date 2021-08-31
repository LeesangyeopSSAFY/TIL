# 직사각형 네 개의 합집합 면적 구하기
plate = [[0]*101 for _ in range(101)]
for i in range(4):
    r1, c1, r2, c2 = map(int, input().split())
    for r in range(r1, r2):
        for c in range(c1, c2):
            plate[r][c] += 1

area = 0
for x in range(101):
    for y in range(101):
        if plate[x][y] >= 1:
            area += 1

print(area)