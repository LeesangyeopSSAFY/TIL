N = int(input())

cnt = 0
val = 666
while cnt < N:
    tmp = str(val)
    if '666' in tmp:
        cnt += 1
    val += 1

print(val-1)