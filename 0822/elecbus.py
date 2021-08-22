T = int(input())
for t in range(1, T+1):
    K, N, M = map(int, input().strip().split())
    charges = [0] * N
    charges_input = list(map(int, input().split()))
    for charge_idx in charges_input:
        charges[charge_idx] += 1
    
    bus_stop = 0
    charge_num = 0
    while bus_stop < N:
        if (N - bus_stop) <= K:
            break
        for k in range(K, 0, -1):
            if charges[bus_stop + k] == 1:
                charge_num += 1
                bus_stop += K
                break
        else:
            charge_num = 0
            break
    print("#{} {}".format(t, charge_num))