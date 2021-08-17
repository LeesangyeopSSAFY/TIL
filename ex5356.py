T = int(input())
for t in range(1, T+1):
    big_list = []
    for _ in range(5):
        small_list = []
        small_list.extend(input())
        big_list.append(small_list)

    new_list = []
    # 각 줄의 길이가 다 다르니 길이의 최대값인 15까지 순회
    for i in range(15):
        # j는 주어지는 다섯 줄을 순회
        for j in range(5):
            try:
                new_list += big_list[j][i]
            # 인덱스를 벗어날 경우에 continue
            except IndexError:
                continue

    print("#{} {}".format(t, ''.join(new_list)))