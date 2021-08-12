T = int(input())
cnt = 0
ans_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for t in range(T):
    cnt += 1
    tc_list = list(map(int, input().split()))
    N = tc_list[0]
    K = tc_list[1]
    total = 0
    totals = []
    for n in range(N):
        scores = list(map(int, input().split()))
        total = scores[0]*0.35 + scores[1]*0.45 + scores[2]*0.2
        totals.append(total)
    new_totals = sorted(totals)
    new_totals.reverse()
    K_score = new_totals.index(totals[K-1])
    
    print(f'#{cnt} {ans_list[K_score // (N//10)]}')