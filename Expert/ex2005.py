T = int(input())
cnt = 0
for t in range(T):
    cnt += 1
    N = int(input())
    trow = [1]
    y = [0]
    for n in range(N):
        print(trow)
        trow=[left+right for left,right in zip(trow+y, y+trow)] # 구글링
    n += 1

    