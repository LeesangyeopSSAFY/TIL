# 삼성시의 버스 노선 구하기
T = int(input())
for t in range(1, T+1):
    N = int(input())
    nosun_list = [0]*5001 # 각 정류장을 지나가는 노선을 카운트
    for n in range(N):
        A, B = map(int, input().split())
        # Ai부터 Bi까지 각 정류장을 지나는 노선 카운트
        for nosun in range(A, B+1):
            nosun_list[nosun] += 1

    P = int(input())
    p_list = []
    # P개의 버스 정류장을 확인하는 리스트 생성
    for _ in range(P):
        p = int(input())
        p_list.append(p)

    print("#{}".format(t), end=" ")
    # 각 정류장별 버스 노선의 개수 출력
    for nosun_cnt in p_list:
        print(nosun_list[nosun_cnt], end=" ")
    print()