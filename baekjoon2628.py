garo, sero = map(int, input().split())
N = int(input())
row_idx = [0]
col_idx = [0]
for n in range(N):
    dir, idx = map(int, input().split())
    if dir == 0:
        row_idx.append(idx)
    else:
        col_idx.append(idx)
row_idx.append(sero)
col_idx.append(garo)

row_idx.sort()
col_idx.sort()
area_list = []
# 4중 for문을 사용한 것은 각 범위 별로 영역을 카운트 하기 위함
for r in range(len(row_idx)-1):
    for c in range(len(col_idx)-1):
        cnt = 0
        for s in range(row_idx[r+1]-row_idx[r]):
            for g in range(col_idx[c+1]-col_idx[c]):
                cnt+= 1
        area_list.append(cnt)

print(max(area_list))