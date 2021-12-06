# 모의 SW 역량테스트
# 점심 식사시간
def Calculation(stair_list, stair):
    # cnt: 시간, d_cnt: 대기인원
    cnt, d_cnt = 0, 0
    Q = []
    while stair_list or Q or d_cnt:
        # 대기하는 사람이 있다면
        while d_cnt:
            # 인원이 다 찼다면 정지
            if len(Q) == 3:
                break
            # 내려가는 사람들에게 넣어주기
            Q.append(stair[2])
            d_cnt -= 1
        
        # 내려가는 인원이 있을 때
        for i in range(len(Q)-1, -1, -1):
            # 시간을 감소
            Q[i] -= 1
            # 아래층에 도착했다면 빼기
            if Q[i] <= 0:
                Q.pop(i)
        
        # 이동중인 사람이 있다면
        for i in range(len(stair_list)-1, -1, -1):
            # 거리를 감소시키고
            stair_list[i] -= 1
            # 계단에 도착했다면
            if stair_list[i] <= 0:
                # 빼고 대기인원 추가
                stair_list.pop(i)
                d_cnt += 1
        
        cnt += 1
    return cnt

def dfs(idx):
    global min_count
    if idx == Num:
        stair_list1, stair_list2 = [], []
        for i in range(Num):
            # 1번 계단으로 가는 사람 리스트
            if where_to_go[i]:
                stair_list1.append(Peoples[i][0])
            # 2번 계단으로 가는 사람 리스트
            else:
                stair_list2.append(Peoples[i][1])
        
        time = max(Calculation(sorted(stair_list1), Stairs[0]), Calculation(sorted(stair_list2), Stairs[1]))
        min_count = min(time, min_count)
        return
    
    where_to_go[idx] = False
    dfs(idx+1)
    where_to_go[idx] = True
    dfs(idx+1)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    Peoples = [] # 사람위치
    Stairs = [] # 계단위치와 계단길이  
    Num = 0 # 사람수
    min_count = 987654321 # 소요되는 최소 시간
    for i in range(N):
        for j in range(N):
            if room[i][j]:
                # 사람이라면
                if room[i][j] == 1:
                    Num += 1
                    Peoples.append([i, j])
                # 계단이면
                else:
                    Stairs.append([i, j, room[i][j]])
    
    for i in range(len(Peoples)):
        dis1 = abs(Peoples[i][0] - Stairs[0][0]) + abs(Peoples[i][1] - Stairs[0][1])
        dis2 = abs(Peoples[i][0] - Stairs[1][0]) + abs(Peoples[i][1] - Stairs[1][1])
        Peoples[i][0] = dis1
        Peoples[i][1] = dis2
    
    # 어느 계단으로 갈것인지
    where_to_go = [False for _ in range(Num)]
    dfs(0)
    print('#{} {}'.format(t, min_count+1))

