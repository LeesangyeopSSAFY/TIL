t = int(input())
num_lists = []
cnt = 0

for i in range(t):
    num_lists.append(list(map(int,input().split())))


for num_list in num_lists:
    max_num = num_list[0]
    for j in range(len(num_list)):
        if num_list[j] > max_num:
            max_num = num_list[j]
    cnt += 1
    print(f'#{cnt} {max_num}')
            
