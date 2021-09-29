'''
01D06079861D79F99F
0000000 1110100 0001100 0000111 1001100 0011000 0111010 1111001 1111100 1100111 11
'''

inp_16 = input()
arr_2 = ''
for i in inp_16:
    if i == '0': arr_2 += '0000'
    elif i == '1': arr_2 += '0001'
    elif i == '2': arr_2 += '0010'
    elif i == '3': arr_2 += '0011'
    elif i == '4': arr_2 += '0100'
    elif i == '5': arr_2 += '0101'
    elif i == '6': arr_2 += '0110'
    elif i == '7': arr_2 += '0111'
    elif i == '8': arr_2 += '1000'
    elif i == '9': arr_2 += '1001'
    elif i == 'A': arr_2 += '1010'
    elif i == 'B': arr_2 += '1011'
    elif i == 'C': arr_2 += '1100'
    elif i == 'D': arr_2 += '1101'
    elif i == 'E': arr_2 += '1110'
    elif i == 'F': arr_2 += '1111'

end_point = len(arr_2)//7
idx=0
ans = 0
while idx < len(arr_2):
    # 7의 배수일 때
    if idx <= (end_point-1)*7:
        ans += int(arr_2[idx]) * (2**6)
        ans += int(arr_2[idx+1]) * (2**5)
        ans += int(arr_2[idx+2]) * (2**4)
        ans += int(arr_2[idx+3]) * (2**3)
        ans += int(arr_2[idx+4]) * (2**2)
        ans += int(arr_2[idx+5]) * (2**1)
        ans += int(arr_2[idx+6]) * (2**0)
        print(ans, end=', ')
        ans = 0
    # 나머지가 있을 때
    else:
        remainder = len(arr_2) - end_point*7
        for r in range(remainder):
            ans += int(arr_2[-r-1]) * 2**(r)
        print(ans)
    idx += 7
    
    
