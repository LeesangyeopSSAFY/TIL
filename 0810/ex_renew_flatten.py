for t in range(1, 11):
    dump_num = int(input())
    box_input = list(map(int, input().strip().split()))
    idx_list = [0] * len(box_input)
    # 각 idx의 박스 높이 구하기
    for idx in box_input:
        idx_list[idx-1] += 1

    # 최저점과 최고점 idx 구하기
    for i in range(len(box_input)):
        if idx_list[i]:
            min_idx = i
            break
    for j in range(len(box_input)-1, -1, -1):
        if idx_list[j]:
            max_idx = j
            break

    while dump_num > 0:
        if max_idx - min_idx > 1:
            idx_list[min_idx] -= 1
            idx_list[min_idx+1] += 1
            idx_list[max_idx] -= 1
            idx_list[max_idx-1] += 1
            dump_num -= 1
        else:
            break

        # 최저점과 최고점의 높이가 0이 될 경우
        if idx_list[min_idx] == 0:
            min_idx += 1
        if idx_list[max_idx] == 0:
            max_idx -= 1


    print("#{} {}".format(t, max_idx-min_idx))