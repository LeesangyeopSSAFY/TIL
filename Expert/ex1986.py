T = int(input())
cnt = 0
for t in range(T):
    N = int(input())
    total = 0
    for n in range(1, N+1):
        if n % 2:
            total += n
        else:
            total -= n
    cnt += 1
    print(f'#{cnt} {total}')