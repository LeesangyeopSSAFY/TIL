# 연구소
import sys
from collections import deque
import copy
input = sys.stdin.readline
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
maxi = 0 # 안정 영역의 크기의 최댓값을 구하는 변수

def bfs(arr):
    q = deque([])
    visited = [[False]*M for _ in range(N)]
    cnt = 0
    global maxi

    for virus in list_2:
        q.append(virus)

    while q:
        curr_r, curr_c = q.popleft()

        for dir in range(4):
            nr = curr_r + dr[dir]
            nc = curr_c + dc[dir]

            if nr < 0 or nr >= N or nc < 0 or nc >= M: # 범위 체크
                continue
            if arr[nr][nc] == 0 and not visited[nr][nc]:
                arr[nr][nc] = 2
                visited[nr][nc] = True
                q.append([nr, nc])

    # 안전 영역의 갯수를 카운트 해서
    for i in range(N):
        cnt += arr[i].count(0)

    # 최댓값 비교
    if cnt > maxi:
        maxi = cnt                


N, M = map(int, input().split())
lab = []
for _ in range(N):
    lab.append(list(map(int, input().split())))

list_0 = [] # 빈 칸 리스트
list_2 = [] # 바이러스 있는 곳 리스트
for n in range(N):
    for m in range(M):
        if lab[n][m] == 0:
            list_0.append([n, m])
        elif lab[n][m] == 2:
            list_2.append([n, m])

# 가능한 조합 만들기
for i in range(len(list_0)-2):
    for j in range(i+1, len(list_0)-1):
        for k in range(j+1, len(list_0)):
            r1, c1 = list_0[i]
            r2, c2 = list_0[j]
            r3, c3 = list_0[k]

            # 비어있는 곳 3곳에 벽을 만들기
            lab[r1][c1] = 1
            lab[r2][c2] = 1
            lab[r3][c3] = 1

            # bfs 돌면 2차원 리스트가 변형되니 카피해서 bfs할 리스트 복사
            bfs_lab = copy.deepcopy(lab)
            bfs(bfs_lab)

            # 다시 복원
            lab[r1][c1] = 0
            lab[r2][c2] = 0
            lab[r3][c3] = 0

print(maxi)





