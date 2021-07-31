# 백만 장자 프로젝트
T = int(input())
cnt = 0
for t in range(T):
    N = int(input())
    N_list = list(map(int, input().split()))
    biggest = N_list[-1] #마지막 값을 가장 큰 값으로 설정
    revenue = 0
    for i in range(len(N_list)-1, -1, -1): #뒤에서부터 순환
        if biggest > N_list[i]: # 가장 큰 값이 i번째 값보다 클 경우
            revenue += biggest - N_list[i] #revenue에 차이만큼 더함
        else: #가장 큰 값이 i번째 값보다 작거나 같을 때
            biggest = N_list[i] # 가장 큰 값을 i번째 값으로 변경
    cnt += 1
    print(f'#{cnt} {revenue}')
