T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    # 둘 다 오름차순 정렬
    weight.sort()
    truck.sort()
    ans = 0
    # 거꾸로 돌면서
    for w in range(len(weight)-1, -1, -1):
        for t in range(len(truck)-1, -1, -1):
            # 트럭 적재용량이 화물 무게보다 크거나 같으면
            if truck[t] >= weight[w]:
                # ans에 무게 추가하고
                ans += weight[w]
                # 중복될 수 있으니 한 번 쓴 트럭은 0으로 바꿈
                truck[t] = 0
                # break가 없으면 한 반복문에 계속 큰 트럭이 0으로 바뀌므로 break 걸어주기
                break

    print('#{} {}'.format(tc, ans))