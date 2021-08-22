T = int(input())
for t in range(1, T+1):
    N = int(input())
    tenten = [[0]*10 for _ in range(10)]

    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                tenten[r][c] += color
    
    cnt = 0
    for r_line in tenten: #2차원 배열인 tenten에서 각 요소인 r_line을 순회하면서
        for ch_bora in r_line: #1차원 배열 r_line을 순회하면서 보라색인지 체크
            if ch_bora == 3:
                cnt += 1
    
    print(cnt)