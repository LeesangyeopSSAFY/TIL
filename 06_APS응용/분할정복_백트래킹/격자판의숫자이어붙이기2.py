dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def search(r, c):
    stack = []    
    stack.append((r, c, arr[r][c]))
    while stack:
        r, c, tmp = stack.pop()

        if len(tmp) == 7:
            num_set.add(tmp)
            continue
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 4 and 0 <= nc < 4:
                stack.append((nr, nc, tmp+arr[nr][nc]))

T = int(input())
for t in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    num_set = set()
    for i in range(4):
        for j in range(4):
            search(i, j)
    print('#{} {}'.format(t, len(num_set)))