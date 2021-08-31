# 방배정
girls = [0] * 7
boys = [0] * 7
N, K = map(int, input().split())
for _ in range(N):
    S, Y = map(int, input().split())
    if S == 0:
        girls[Y] += 1
    elif S == 1:
        boys[Y] += 1
room = 0
for g in range(1, 7):
    if girls[g] > 0:
        room += (girls[g]-1)//K + 1

for b in range(1, 7):
    if boys[b] > 0:
        room += (boys[b]-1)//K + 1

print(room)