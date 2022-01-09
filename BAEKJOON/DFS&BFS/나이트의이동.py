T = int(input())
for _ in range(T):
    l = int(input())
    plate = [[0]*l for _ in range(l)]
    st = list(map(int, input().split()))
    ed = list(map(int, input().split()))