T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    ans_list = []
    for i in range(1<<N):
        height = 0
        for j in range(N):
            if i & (1<<j): # i의 j번째 비트가 1이면 j번째 원소 출력
                height += heights[j]
        # 값 비교
        if height >= B:
            ans_list.append(height)

    print('#{} {}'.format(t, min(ans_list)-B))