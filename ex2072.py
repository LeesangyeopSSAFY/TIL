t = int(input())
num_lists = []
result_cnt = 0

for i in range(t):
    num_lists.append(list(map(int,input().split())))

for j in num_lists:
    result_sum = 0
    result_num = 0
    for k in j:
       result_sum += k
       result_num += 1
    result_cnt += 1
    print('#{0} {1:.0f}'.format(result_cnt, result_sum/result_num))