T = int(input())
cnt = 0
for t in range(T):
    cnt += 1
    ten_list = list(map(int, input().split()))
    # .remove()메서드를 통해 최대값과 최소값을 제거
    ten_list.remove(max(ten_list))
    ten_list.remove(min(ten_list))
    print(f'#{cnt} {round(sum(ten_list)/len(ten_list))}')
