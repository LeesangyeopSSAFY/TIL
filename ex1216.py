def mkmax_pal(list_input): #최대 길이를 가지는 회문의 길이 반환 함수
    max_pal = 0
    # 큰 리스트의 문자열이나 리스트를 순회하면서
    for r in list_input:
        #i는 0부터 99까지 오름차순
        for i in range(100):
            #j는 99부터 i까지 내림차순
            for j in range(99, i-1, -1):
                word = r[i:j+1]
                # i부터 j까지 길이의 회문이고 max_pal보다 크다면
                if word == word[::-1] and len(word)>max_pal:
                    max_pal = len(word)
    return max_pal

T = 10
for t in range(1, T+1):
    tc_num = int(input())
    str_plate = []
    for _ in range(100):
        str_plate.append(input())
    # 행과 열을 뒤집은 new_plate리스트 생성
    new_plate = []
    for new1 in range(100):
        new_plate.append([0]*100)

    for a in range(100):
        for b in range(100):
            new_plate[a][b] = str_plate[b][a] # 로꾸거

    max1 = mkmax_pal(str_plate)
    max2 = mkmax_pal(new_plate)
    if max1 > max2:
        print("#{} {}".format(tc_num, max1))
    else:
        print("#{} {}".format(tc_num, max2))