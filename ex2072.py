t = int(input())
num_lists = []
cnt = 0

for i in range(t):
    num_lists.append(list(map(int, input().split())))

for num_list in num_lists:
    result = 0
    cnt += 1
    for number in num_list:
        if number % 2:
            result += number
    print(f'#{cnt} {result}')
