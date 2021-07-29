N = int(input())
N_list = list(map(int,input().split()))

#sorted()함수를 통해 정렬
N_list_sort = sorted(N_list)
#정렬한 리스트의 중간자리를 반환
mid_num = N_list_sort[len(N_list)//2]
print(mid_num)
