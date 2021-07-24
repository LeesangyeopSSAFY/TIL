# word = 'apple'
# new_word = ''
# for i in range(1, len(word)+1):
#     new_word += word[-i]
# print(new_word)

# n = int(input())
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i, end=' ')

numbers1 = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
    51, 61, 63, 87, 66, 24, 80, 83, 71, 60 , 64,
    52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
]
number = sorted(numbers1)
if (len(number)) % 2 == 0:
    mid_inx = (len(nubmer) / 2)
    mid_value = number[mid_inx]
    print(mid_value)
else:
    mid_inx = int(len(number) / 2)
    mid_value = number[mid_inx]
    print(mid_value)

