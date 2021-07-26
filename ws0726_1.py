def count_blood(blood_list):
    # .count() 메서드를 통해 각 혈액형 별 개수를 카운트 
    A_num = blood_list.count('A')
    B_num = blood_list.count('B')
    O_num = blood_list.count('O')
    AB_num = blood_list.count('AB')
    # 카운트한 혈액형 별 key, value를 가진 blood_dict 생성
    blood_dict = {
        'A': A_num,
        'B': B_num,
        'O': O_num,
        'AB': AB_num
    }
    return blood_dict

print(count_blood(['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']))