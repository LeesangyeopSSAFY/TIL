T = int(input())
for t in range(1, T+1):
    N = int(input())
    room_list = []
    for _ in range(N):
        room_list.append(list(map(int, input().split())))
    time = 1
    while room_list:
        for i in range(len(room_list)-2, -1, -1):
            if room_list[i][0] < room_list[-1][0] < room_list[i][1]:
                time += 1
                room_list.pop()
                break
        else:
            room_list.pop()

    print("#{} {}".format(t, time))