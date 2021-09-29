# 단순 2진 암호코드
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for i in range(N):
        arr.append(input())
    code = ''
    for n in range(N):
        # 뒤에서부터 탐색
        for m in range(M-1, -1, -1):
            # 1이 나오면
            if arr[n][m] == '1':
                # m-55부터 m인덱스까지 7간격으로
                for idx in range(m-55, m+1, 7):
                    if arr[n][idx:idx+7] == '0001101':
                        code += '0'
                    elif arr[n][idx:idx+7] == '0011001':
                        code += '1'
                    elif arr[n][idx:idx+7] == '0010011':
                        code += '2'
                    elif arr[n][idx:idx+7] == '0111101':
                        code += '3'
                    elif arr[n][idx:idx+7] == '0100011':
                        code += '4'
                    elif arr[n][idx:idx+7] == '0110001':
                        code += '5'
                    elif arr[n][idx:idx+7] == '0101111':
                        code += '6'
                    elif arr[n][idx:idx+7] == '0111011':
                        code += '7'
                    elif arr[n][idx:idx+7] == '0110111':
                        code += '8'
                    elif arr[n][idx:idx+7] == '0001011':
                        code += '9'
                break
        # 한 번 코드가 생성되면 break
        if code:
            break

    ans = 0
    total = 0
    for i in range(8):
        # 홀수 인덱스는 그냥 더하기
        if i%2:
            total += int(code[i])
            ans += int(code[i])
        # 짝수 인덱스는 3배를 더하기
        else:
            total += int(code[i]) * 3
            ans += int(code[i])
    # 총 합이 10의 배수이면
    if total % 10 == 0:
        print('#{} {}'.format(t, ans))
    else:
        print(f'#{t} 0')