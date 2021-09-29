'''
0000000111 1000000110 0000011110 0110000110 0001111001 1110011111 1001100111
0000000 1111000 0001100 0000111 1001100 0011000 0111100 1111001 1111100 1100111
'''

arr = list(input().split())
tmp = ''
for i in arr:
    tmp += i


for idx in range(0, len(tmp), 7):
    ans = 0
    ans += int(tmp[idx]) * (2**6)
    ans += int(tmp[idx+1]) * (2**5)
    ans += int(tmp[idx+2]) * (2**4)
    ans += int(tmp[idx+3]) * (2**3)
    ans += int(tmp[idx+4]) * (2**2)
    ans += int(tmp[idx+5]) * (2**1)
    ans += int(tmp[idx+6]) * (2**0)
    if idx == len(tmp)-7:
        print(ans)
    else:
        print(ans, end=', ')