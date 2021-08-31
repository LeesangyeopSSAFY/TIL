# 가랏!RC카!

T = int(input())
for t in range(1, T+1):
    N = int(input())
    v = 0
    s = 0
    for n in range(N):
        a = input()
        if len(a) == 1:
            s += v
        else:
            if a[0] == '1':
                v += int(a[2])
                s += v
            elif a[0] == '2':
                if v >= int(a[2]):
                    v -= int(a[2])
                    s += v
                else:
                    v = 0
    print("#{} {}".format(t, s))
