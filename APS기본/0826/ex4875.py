T = int(input())
for t in range(1, T+1):
    N = int(input())
    miro = []
    for _ in range(N):
        miro.append(list(input().strip()))
    # 출발점 찾기
    for i in range(N):
        for j in range(N):
            if miro[i][j] == '2':
                sr = i
                sc = j

    dr = [-1, 1, 0, 0] #상하좌우
    dc = [0, 0, -1, 1]
    stack = [(sr, sc)]
    ans = 0
    while stack:
        r, c = stack.pop()
        for dir in range(4): # 4방향 중 갈 수 있는 방향 체크
            nr = r + dr[dir]
            nc = c + dc[dir]
            if 0 <= nr < N and 0 <= nc < N: # 가고자 하는 방향이 범위 안에 있고
                if miro[nr][nc] == '0': # 통로이면
                    stack.append((nr, nc)) # 스택에 추가
                    miro[nr][nc] = 'visted' # 방문한 곳 체크
                elif miro[nr][nc] == '3': # 도착점에 도달하면
                    ans = 1
                    stack.clear() # while문을 끝내기 위해
                    break


    print("#{} {}".format(t, ans))
