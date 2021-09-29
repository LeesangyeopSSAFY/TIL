# a = 102
# b = 33
# c = 33

# print(a^b) # 다르면 0이 아니고,
# print(b^c) # 같으면 0이 나온다

# if b == c:
#     print('같음')

# if b^c == 0:
#     print('같음')

# 짝수, 홀수를 알 수 있다.
# print(a&1)
# print(b&1)

# if a & 0x01:
#     print('홀수')
# else:
#     print('짝수')

for i in range(1<<3):
    # if i & (1<<0):  # 0이 아니면
    #     print(f'{i}의 0번 비트는 1')
    # else:
    #     print(f'{i}의 0번 비트는 0')
    print(f'{i}의 2번 비트는 {(i&(1<<2))>>2}')