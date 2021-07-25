# ans = []
# for a in range(1, 101):
#     if a % 2 == 0:
#         ans += [str(a)]
# print(' '.join(ans))

data = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
result = {}
for i in data:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
print(result)