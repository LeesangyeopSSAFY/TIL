T = int(input())
cnt = 0
for t in range(T):
    cnt += 1
    str_list = []
    new_word = []
    str_list.extend(input())
    for i in range(len(str_list)-1, -1, -1):
        new_word += str_list[i]
    if new_word == str_list:
        print(f'#{cnt} 1')
    else:
        print(f'#{cnt} 0')


# for case in str_list:
#     new_word = case.reverse()
#     if new_word == case:
#         print('1')
#     else:
#         print('0')

    # result = True
    # for i in range(int(len(case)/2)):
    #     for j in range(len(case)//2):
    #         if case[j] != case[-j-1]:
    #             result = result and False
    #         else:
    #             result = result and True

    # print(result)
    