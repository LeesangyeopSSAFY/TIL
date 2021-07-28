N = int(input())
N_list = list(map(int,input().split()))

N_list_sort = sorted(N_list)
mid_num = N_list_sort[len(N_list)//2]
print(mid_num)
