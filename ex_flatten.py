T = 10
for t in range(1, T+1):
    N = int(input())
    test_list = list(map(int, input().split()))
    # N번 순환
    for n in range(N):
        # 버블 정렬
        for i in range(len(test_list)-1, 0, -1):
            for j in range(i):
                if test_list[j] > test_list[j+1]:
                    test_list[j], test_list[j+1] = test_list[j+1], test_list[j]
        # 첫번째 값 +1 마지막 값 -1
        test_list[0] = test_list[0] + 1
        test_list[-1] = test_list[-1] -1
    mini = 0
    maxi = 0
    # 첫번째 값이 그 다음 값보다 작거나 같다면 그대로
    if test_list[0] <= test_list[1]:
        mini = test_list[0]
    else:
        mini = test_list[1]

    # 마지막 값이 그 전 값보다 크거나 같다면 그대로
    if test_list[-1] >= test_list[-2]:
        maxi = test_list[-1]
    else:
        maxi = test_list[-2]
    print("#{} {}".format(t, maxi - mini))