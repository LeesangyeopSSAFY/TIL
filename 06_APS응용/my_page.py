T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        tmp = input().strip()
        if tmp != '0'*M and not tmp.strip('0') in arr:
            arr.append(tmp.strip('0'))

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] in arr[j]:
                arr[j] = arr[j].replace(arr[i], '0', 1).strip('0')
    
    for x in range(len(arr)):
        for m in range(M//8 + 1):
            if 8*m < len(arr[x]) < 8*(m+1):
                arr[x] = '0'*(8*(m+1)-len(arr[x])) + arr[x]
    
    ans_list = []
    for i in range(len(arr)):
        code = ''
        for j in range(len(arr[i])):
            if arr[i][j] == '0': code += '0000'
            elif arr[i][j] == '1': code += '0001'
            elif arr[i][j] == '2': code += '0010'
            elif arr[i][j] == '3': code += '0011'
            elif arr[i][j] == '4': code += '0100'
            elif arr[i][j] == '5': code += '0101'
            elif arr[i][j] == '6': code += '0110'
            elif arr[i][j] == '7': code += '0111'
            elif arr[i][j] == '8': code += '1000'
            elif arr[i][j] == '9': code += '1001'
            elif arr[i][j] == 'A': code += '1010'
            elif arr[i][j] == 'B': code += '1011'
            elif arr[i][j] == 'C': code += '1100'
            elif arr[i][j] == 'D': code += '1101'
            elif arr[i][j] == 'E': code += '1110'
            elif arr[i][j] == 'F': code += '1111'
        code = code.strip('0')
        code = '0'*(56 - (len(code)%56)) + code
        multi = len(code)//56
        code2 = ''
        for c in range(0, len(code), 7*multi):
            if code[c:c+7*multi] == '000'*multi + '11'*multi + '0'*multi + '1'*multi: code2 += '0'
            elif code[c:c+7*multi] == '00'*multi + '11'*multi + '00'*multi + '1'*multi: code2 += '1'
            elif code[c:c+7*multi] == '00'*multi + '1'*multi + '00'*multi + '11'*multi: code2 += '2'
            elif code[c:c+7*multi] == '0'*multi + '1111'*multi + '0'*multi + '1'*multi: code2 += '3'
            elif code[c:c+7*multi] == '0'*multi + '1'*multi + '000'*multi + '11'*multi: code2 += '4'
            elif code[c:c+7*multi] == '0'*multi + '11'*multi + '000'*multi + '1'*multi: code2 += '5'
            elif code[c:c+7*multi] == '0'*multi + '1'*multi + '0'*multi + '1111'*multi: code2 += '6'
            elif code[c:c+7*multi] == '0'*multi + '111'*multi + '0'*multi + '11'*multi: code2 += '7'
            elif code[c:c+7*multi] == '0'*multi + '11'*multi + '0'*multi + '111'*multi: code2 += '8'
            elif code[c:c+7*multi] == '000'*multi + '1'*multi + '0'*multi + '11'*multi: code2 += '9'
        
        ans = 0
        total = 0
        for i in range(8):
            if i%2:
                total += int(code2[i])
                ans += int(code2[i])
            else:
                total += int(code2[i]) * 3
                ans += int(code2[i])
        
        if total % 10 == 0:
            ans_list.append(ans)
        else:
            ans_list.append(0)
    
    if 0 in ans_list:
        print(f'#{t} 0')
    else:
        print('#{} {}'.format(t, sum(ans_list)))