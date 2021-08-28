# 정곤이의 단조 증가하는 수

T = int(input())
for t in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().strip().split()))
    danzo_list = []
    for i in range(N-1):
        for j in range(i+1, N):
            product = str(num_list[i] * num_list[j])
            danzo = 1
            for k in range(1, len(product)):
                if int(product[k]) < int(product[k-1]):
                    danzo = 0
                    break
            if danzo == 1:
                danzo_list.append(int(product))

    if danzo_list:
        print("#{} {}".format(t, max(danzo_list)))
    else:
        print("#{} -1".format(t))