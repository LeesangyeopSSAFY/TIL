import copy
def bank(val):
    # val가 3진수 초기값보다 크면
    if first_valB < val:
        for b in range(len(B)):
            # 인덱스 값을 바꾸려고 deepcopy
            testB = copy.deepcopy(B)
            # 각 자리 수가 2가 되면 그 인덱스를 변경했을 때 가장 큰 값이 되므로 2가 될 때까지 1씩 더해주기
            while testB[b] != 2:
                testB[b] = (testB[b] + 1) % 3
                val_B = 0
                for i in range(len(testB)):
                    val_B += testB[i] * 3**(len(testB)-1-i)
                # 바꾼 후 10진수로 계산해보고 val랑 같으면 True를 반환
                if val_B == val:
                    return True
    # val가 3진수 초기값과 작으면
    elif first_valB > val:
        for b in range(len(B)):
            testB2 = copy.deepcopy(B)
            # 각 자리 수가 0이 되면 해당 인덱스를 변경했을 때 가장 작은 값이 되므로 0이 될 때까지 1씩 빼주기
            while testB2[b] != 0:
                testB2[b] = (testB2[b] - 1) % 3
                val_B2 = 0
                for i in range(len(testB2)):
                    val_B2 += testB2[i] * 3**(len(testB2)-1-i)
                if val_B2 == val:
                    return True
    return



T = int(input())
for tc in range(1, T+1):
    tmp_A = input()
    tmp_B = input()
    A = []
    B = []
    for tmp_a in tmp_A:
        A.append(int(tmp_a))
    first_valB = 0 # 처음 3진수의 값
    for tmp_b in range(len(tmp_B)):
        first_valB += int(tmp_B[tmp_b]) * 3**(len(tmp_B)-1-tmp_b)
        B.append(int(tmp_B[tmp_b]))

    for i in range(len(A)):
        # 각 인덱스의 값으 변경
        A[i] = (A[i] + 1) % 2
        val = 0
        # 2진수의 각 자리를 하나씩 바꾸면서 나온 값을 bank 함수로 검사
        for j in range(len(A)):
            val += A[j] * 2**(len(A)-1-j)
        # bank에서 True가 나온다면
        if bank(val):
            ans = val
            break
        # 바꾼 인덱스의 값을 다시 원상복구
        A[i] = (A[i] + 1) % 2

    print('#{} {}'.format(tc, ans))