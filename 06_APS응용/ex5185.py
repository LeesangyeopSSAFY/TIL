T = int(input())
for t in range(1, T+1):
    N, tc = input().split()
    N = int(N)
    ans = ''
    for i in tc:
        if i == '0': ans += '0000'
        elif i == '1': ans += '0001'
        elif i == '2': ans += '0010'
        elif i == '3': ans += '0011'
        elif i == '4': ans += '0100'
        elif i == '5': ans += '0101'
        elif i == '6': ans += '0110'
        elif i == '7': ans += '0111'
        elif i == '8': ans += '1000'
        elif i == '9': ans += '1001'
        elif i == 'A': ans += '1010'
        elif i == 'B': ans += '1011'
        elif i == 'C': ans += '1100'
        elif i == 'D': ans += '1101'
        elif i == 'E': ans += '1110'
        elif i == 'F': ans += '1111'
    print('#{} {}'.format(t, ans))