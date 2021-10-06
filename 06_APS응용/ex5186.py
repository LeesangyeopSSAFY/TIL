# 이진수2
T = int(input())
for t in range(1, T+1):
    N = float(input())
    tmp = N
    ans_list=[]
    # 12자리를 돌면서
    for i in range(1, 13):
        # 남은 값이 2^(-i)보다 크거나 같으면
        if 2**(-i) <= tmp:
            # 그만큼 빼주고
            tmp = tmp - 2**(-i)
            # ans_list에 1을 추가
            ans_list += '1'
        # 남은 값이 2^(-i)보다 작으면 ans_list에 0 추가
        else:
            ans_list += '0'
        # 답이 구해지면 break
        if tmp == 0:
            break
    
    ans = "".join(ans_list)
    # 13자리 이상이 필요한 경우
    if tmp:
        print(f'#{t} overflow')
    else:
        print('#{} {}'.format(t, ans))