T = int(input())
for t in range(1, T+1):
    R, C = map(int, input().split())
    sea = []
    for _ in range(R):
        tmp = list(map(int, input().split()))
        sea.append(tmp)
    print(sea)