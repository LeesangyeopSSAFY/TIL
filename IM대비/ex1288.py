# 새로운 불면증 치료법

T = int(input())
for t in range(1, T+1):
    N = int(input())
    k = 0
    num_check = [0]*10
    while num_check != [1]*10:
        k += 1
        kN = k * N
        num = str(kN)
        for n in range(len(num)):
            if num_check[int(num[n])] == 0:
                num_check[int(num[n])] = 1
    print("#{} {}".format(t, kN))