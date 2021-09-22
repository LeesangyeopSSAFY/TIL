def lonely(first_list):
    for i in range(len(first_list)-1, 0, -1): # list의 마지막 순서부터 차례로 내려오면서
        if first_list[i] == first_list[i-1]: # list의 i번째 값이 그 전 값과 같다면
            first_list.pop(i) # i 위치의 값을 삭제
    return first_list

print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))