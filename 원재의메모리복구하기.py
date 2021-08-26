T = int(input())
for t in range(1, T+1):
    memory = input()
    f_idx = memory.find('1') # 처음 1이 나오는 인덱스를 찾기
    fix = 1 #고치는 횟수인 fix를 1로 설정
    for i in range(f_idx+1, len(memory)): # f_idx다음 인덱스부터 끝까지 중에
        if memory[i] != memory[i-1]: # 그 전 값과 비트가 다른 경우
            fix += 1 # fix에 1추가
    print("#{} {}".format(t, fix))

