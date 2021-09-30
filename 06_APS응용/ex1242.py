# 암호코드 스캔
# 16진수를 2진수로 바꾸는
htob = {
    '0':'0000', '1':'0001', '2':'0010', '3':'0011',
    '4':'0100', '5':'0101', '6':'0110', '7':'0111',
    '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
    'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'
}

# 암호 패턴 비율 딕셔너리
pattern_dict = {
    "211": 0,
    "221": 1,
    "122": 2,
    "411": 3,
    "132": 4,
    "231": 5,
    "114": 6,
    "312": 7,
    "213": 8,
    "112": 9,
}

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    tmp = [input() for _ in range(N)]
    tmp_list = list(set(tmp)) # 중복되는 열 제거
    
    # 2진수로 변환
    tmp_list_b = [""] * len(tmp_list)
    for i in range(len(tmp_list)):
        for j in range(M):
            tmp_list_b[i] += htob[tmp_list[i][j]]
    
    code_list = []
    for data in tmp_list_b:
        # 0으로만 이루어진 행이 아니라면
        if int(data) != 0:
            code_list.append(data)
    
    ans = 0
    visited = []
    for code in code_list:
        PW = []
        # 비율을 구하기 위한 변수 설정
        a = b = c = d = 0
        code = code.rstrip("0")
        for i in range(len(code)-1, -1, -1):
            # 뒤에서 처음 1이 나왔을 때
            if c == 0 and code[i] == '1':
                d += 1
            # 1이 나온 후 0이 나왔을 때
            elif d != 0 and b == 0 and code[i] == "0":
                c += 1
            # 다시 1이 나왔을 때
            elif a == 0 and code[i] == "1":
                b += 1
            # 다시 0이 나왔을 때
            elif b > 0 and c > 0 and d > 0 and code[i] == '0':
                multi = min(b, c, d)
                key = str(b//multi) + str(c//multi) + str(d//multi)
                PW = [pattern_dict[key]] + PW
                a = b = c = d = 0
            
            if len(PW) == 8:
                # 조건에 부합하고
                if ((PW[0] + PW[2]+ PW[4] + PW[6]) * 3 + PW[1] + PW[3] + PW[5] + PW[7]) % 10 == 0:
                    # 중복된 패턴이 아니라면
                    if PW not in visited:
                        ans += sum(PW)
                        visited.append(PW)
                # PW 초기화
                PW = []
    print('#{} {}'.format(t, ans))









# T = int(input())
# for t in range(1, T+1):
#     N, M = map(int, input().split())
#     code_list = list(set([bin(int(input(), 16))[2:].rstrip('0') for _ in range(N)]))
#     ans_list = []
#     for code in code_list:
#         if len(code) >= 1:
#             multi = 1
#             while True:
#                 if len(code) < multi*56:
#                     code = '0'*(56*multi - len(code)) + code
#                 for c in range(0, len(code), 7*multi):
#                     if code[c:c+7*multi] == '000'*multi + '11'*multi + '0'*multi + '1'*multi: code2 += '0'
#                     elif code[c:c+7*multi] == '00'*multi + '11'*multi + '00'*multi + '1'*multi: code2 += '1'
#                     elif code[c:c+7*multi] == '00'*multi + '1'*multi + '00'*multi + '11'*multi: code2 += '2'
#                     elif code[c:c+7*multi] == '0'*multi + '1111'*multi + '0'*multi + '1'*multi: code2 += '3'
#                     elif code[c:c+7*multi] == '0'*multi + '1'*multi + '000'*multi + '11'*multi: code2 += '4'
#                     elif code[c:c+7*multi] == '0'*multi + '11'*multi + '000'*multi + '1'*multi: code2 += '5'
#                     elif code[c:c+7*multi] == '0'*multi + '1'*multi + '0'*multi + '1111'*multi: code2 += '6'
#                     elif code[c:c+7*multi] == '0'*multi + '111'*multi + '0'*multi + '11'*multi: code2 += '7'
#                     elif code[c:c+7*multi] == '0'*multi + '11'*multi + '0'*multi + '111'*multi: code2 += '8'
#                     elif code[c:c+7*multi] == '000'*multi + '1'*multi + '0'*multi + '11'*multi: code2 += '9'


#             ans = 0
#             total = 0
#             for i in range(8):
#                 if i%2:
#                     total += int(code2[i])
#                     ans += int(code2[i])
#                 else:
#                     total += int(code2[i]) * 3
#                     ans += int(code2[i])

#             if total % 10 == 0:
#                 ans_list.append(ans)
#             else:
#                 ans_list.append(0)
    
#     if 0 in ans_list:
#         print(f'#{t} 0')
#     else:
#         print('#{} {}'.format(t, sum(ans_list)))

