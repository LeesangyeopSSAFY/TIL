def check(j, a, b):
    global flag
    new_bit = bit3[:j] + a + bit3[j+1:]
    _new_bit = int(new_bit, 3)

    new_bit2 = bit3[:j] + b + bit3[j+1:]
    _new_bit2 = int(new_bit2, 3)
    if _new_bit in bit2_list:
        print('#{} {}'.format(t, _new_bit))
        flag = 1
        return
    if _new_bit2 in bit2_list:
        print('#{} {}'.format(t, _new_bit2))
        flag = 1
        return


T = int(input())
for t in range(1, T+1):
    flag = 0
    bit2 = input()
    bit3 = input()

    bit2_int = int(bit2, 2)
    bit2_list = []
    for i in range(len(bit2)):
        bit2_list.append(bit2_int ^ (1<<i))

    for j in range(len(bit3)):
        if bit3[j] == '2':
            check(j, '0', '1')
            if flag:
                break
        elif bit3[j] == '1':
            check(j, '0', '2')
            if flag:
                break
        else:
            check(j, '1', '2')
            if flag:
                break