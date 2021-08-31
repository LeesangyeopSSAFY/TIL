# 참외밭
melon = int(input())
EWSN = []
for i in range(6):
    dir, gill = map(int, input().split())
    EWSN.append(gill)

maxi_x = 0
for i in range(0, 6, 2):
    if EWSN[i] > maxi_x:
        maxi_x = EWSN[i]
        maxx_idx = i
maxi_y = 0
for j in range(1, 6, 2):
    if EWSN[j] > maxi_y:
        maxi_y = EWSN[j]
        maxy_idx = j

# 가로 세로 별 가장 긴 길이의 인접 값들을 제외한다.
EWSN[(maxx_idx-1) % 6] = 0
EWSN[(maxx_idx+1) % 6] = 0
EWSN[(maxy_idx-1) % 6] = 0
EWSN[(maxy_idx+1) % 6] = 0

for rem in range(4):
    EWSN.remove(0)

ans = maxi_x * maxi_y - (EWSN[0] * EWSN[1])
print(ans*melon)