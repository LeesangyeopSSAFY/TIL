# 이진수2
T = int(input())
for t in range(1, T+1):
    N = float(input())
    tmp = N
    ans_list=[]
    for i in range(1, 13):
        if 2**(-i) <= tmp:
            tmp = tmp - 2**(-i)
            ans_list += '1'
        else:
            ans_list += '0'
        if tmp == 0:
            break
    
    ans = "".join(ans_list)
    if tmp:
        print(f'#{t} overflow')
    else:
        print('#{} {}'.format(t, ans))