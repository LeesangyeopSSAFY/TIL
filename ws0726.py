def get_dict_avg(dicts):
    # dicts의 각 value 값을 가지는 value_list 생성
    value_list = dicts.values()
    cnt = 0
    # dicts의 개수 카운트
    for i in dicts:
        cnt += 1
    # value_list의 합을 dicts 개수로 나누어 평균 점수 반환
    return sum(value_list) / cnt

print(get_dict_avg({'python': 80, 'algorithm': 90, 'django': 89, 'web': 83}))