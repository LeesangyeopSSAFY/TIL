# def get_middle_char(str):
#     if len(str) % 2:
#         return str[len(str)//2]
#     else:
#         return str[len(str)//2 - 1 : len(str)//2 + 1]
# print(get_middle_char('ssafy'))
# print(get_middle_char('coding'))

# def ssafy(name, location='서울'):
#     print(f'{name}의 지역은 {location}입니다.')

# ssafy('허준')
# ssafy(location='대전', name='철수')
# ssafy('영희', location='광주')

# def my_func(a, b):
#     c = a + b
#     print(c)
    
# result = my_func(3, 7)

def my_avg(*args):
    total = 0
    cnt = 0
    for arg in args:
        total += arg
        cnt += 1
    ans = total / cnt
    return ans
print(my_avg(77, 83, 95, 80, 70))