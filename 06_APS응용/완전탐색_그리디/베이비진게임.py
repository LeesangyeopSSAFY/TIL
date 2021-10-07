def babygin(arr):
    run = triple = 0
    idx = 0
    while idx < 10:
        # 트리플 검사
        if arr[idx] >= 3:
            triple += 1
            arr[idx] -= 3
            continue
        # 런 검사
        if (idx+2) < 10 and arr[idx] >= 1 and arr[idx+1] >= 1 and arr[idx+2]>= 1:
            run += 1
            arr[idx] -=1
            arr[idx+1]-= 1
            arr[idx+2] -= 1
            continue
        idx += 1
    return run+triple

T = int(input())
for t in range(1, T+1):
    cards = list(map(int, input().split()))
    player1 = [0]*10
    player2 = [0]*10
    winner = 0
    for c in range(12):
        # 짝수 인덱스
        if c%2==0:
            player1[cards[c]] += 1
            # 추가할 때마다 베이비진 검사
            check1 = babygin(player1)
            # 런이나 트리플 중 하나라도 완성되면
            if check1 >= 1:
                winner = 1
                break
        # 홀수 인덱스
        else:
            player2[cards[c]] += 1
            check2 = babygin(player2)
            if check2 >= 1:
                winner = 2
                break

    print('#{} {}'.format(t, winner))