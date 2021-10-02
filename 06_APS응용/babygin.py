six_num = input()
six_list = []
for s in six_num:
    six_list.append(int(s))

possible_list = []
for i1 in range(6):
    for i2 in range(6):
        if i2 != i1:
            for i3 in range(6):
                if i3 != i2 and i3 != i1:
                    for i4 in range(6):
                        if i4 != i3 and i4 != i2 and i4 != i1:
                            for i5 in range(6):
                                if i5 != i4 and i5 != i3 and i5 != i2 and i5 != i1:
                                    for i6 in range(6):
                                        possible_list.append([six_list[i1], six_list[i2], six_list[i3], six_list[i4], six_list[i5], six_list[i6]])

print(possible_list)