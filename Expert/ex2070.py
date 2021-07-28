t = int(input())
num_lists = []
cnt = 0

for i in range(t):
    num_lists.append(list(map(int,input().split())))

for num_list in num_lists:
    if num_list[0] > num_list[1]:
        result = '>'
    elif num_list[0] < num_list[1]:
        result = '<'
    else:
        result = '='
    cnt += 1
    print(f'#{cnt} {result}')