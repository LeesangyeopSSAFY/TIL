T = 10
for t in range(1, T+1):
    tc_num = int(input())
    eight_list = list(map(int, input().split()))
    dir = [1, 2, 3, 4, 5] # 나머지 연산을 통해서 사이클 돌리기
    d = -1 # dir의 0번째 인덱스부터 시작하려고
    while eight_list[-1] != 0:
        d += 1
        minus = dir[d % 5]
        last_val = eight_list.pop(0)
        if last_val - minus <= 0: #끝에 붙을 수가 0보다 작아지거나 0일 경우
            eight_list.append(0) #0으로 저장해서 암호 호출
        else:
            eight_list.append(last_val - minus)
    print("#{}".format(tc_num), end=" ")
    for i in range(7):
        print(eight_list[i], end=" ")
    print(eight_list[-1])