# N = int(input())
# for i in range(1, N + 1):
#     if N % i == 0:
#         print(i, end=' ')

# numbers1 = [
#     85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
#     51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
#     52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
# ]
# numbers = sorted(numbers1)

# if (len(numbers)) % 2 == 0:
#     mid_inx = (len(numbers)/2)
#     mid_value = numbers[int(mid_inx)]
#     print(f'{mid_value}')
# else:
#     mid_inx = int(len(numbers)/2)
#     mid_value = numbers[int(mid_inx)]
#     print(f'{mid_value}')

# number = int(input())
# i = 1
# while i <= number:
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()
#     i += 1

# holsu_list = range(1, 51)[0:50:2]
# print(list(holsu_list))

# students = {'정성우': 26, '이승훈': 27, '강동옥': 28, '김도훈': 27,
#            '이상엽': 28, '성아영': 25, '황보창': 27, '정인수': 28,
#            '박상준': 29, '전호정': 24, '홍지범': 28
#            }
# print(students)

# n = 5
# m = 9
# for i in range(m):
#     print('*' * n)

# temp = 36.5
# result = '입실 불가' if temp >= 37.5 else '입실 가능'
# print(result)

scores = [80, 89, 99, 83]
total = 0
for i in range(len(scores)):
    total += scores[i]
print(total / len(scores))
