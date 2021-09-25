# def count_vowels(words):
#     cnt = 0
#     a_cnt = words.count('a')
#     e_cnt = words.count('e')
#     i_cnt = words.count('i')
#     o_cnt = words.count('o')
#     u_cnt = words.count('u')
#     cnt = a_cnt + e_cnt + i_cnt + o_cnt + u_cnt

#     return cnt

# print(count_vowels('apple'))
# print(count_vowels('banana'))

def only_square_area(list_1, list_2):
    area_list = []
    for i in list_1:
        for j in list_2:
            if i == j:
                area = i * j
                area_list.append(area)
    return area_list

print(only_square_area([32, 55, 63], [13, 32, 40, 55]))
