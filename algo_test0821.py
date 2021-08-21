def Sort(List_input):
    for i in range(len(List_input)-1, 0, -1):
        for j in range(0, i):
            if List_input[j] > List_input[j+1]:
                List_input[j], List_input[j+1] = List_input[j+1], List_input[j]

def mk_180(lists):
    list_180 = []
    # 행부터 내림차순 반복
    for r in range(len(lists)-1, -1, -1):
        list_r = []
        # 열 내림차순 반복
        for c in range(len(lists)-1, -1, -1):
            list_r.append(lists[r][c])
        list_180.append(list_r)
    return list_180


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(mk_180(a))