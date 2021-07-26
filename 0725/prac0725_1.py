# a = [0] * 10
# b = int(input())
# result = ""
# while b:
#     a[b%10] += 1
#     b//=10

# for i in range(0, 10):
#     result += f'{i}'
# print(' '.join(result))
# result = ""
# for j in range(10):
#     result += f'{a[j]}'
# print(' '.join(result))

N = input()
result = 0
for i in N:
    result += int(i)
print(result)