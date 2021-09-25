T = 10
for t in range(1, T+1):
    N = int(input())
    arr = [0] * (N+1)
    for n in range(N):
        temp = list(input().split())
        if len(temp) == 4: # 연산자가 있는 경우 arr[i]의 값이 ['연산자', [왼쪽 노드 번호, 오른쪽 노드 번호]]이 되도록 저장
            arr[int(temp[0])] = [temp[1], [int(temp[2]), int(temp[3])]]
        else:
            arr[int(temp[0])] = int(temp[1])


    for i in range(N, 0, -1): # 거꾸로 순회하면서
        if type(arr[i]) != int: # 즉 연산자가 나올 경우
            if arr[i][0] == '+':
                arr[i] = arr[arr[i][1][0]] + arr[arr[i][1][1]] # 각 연산자마다 왼쪽 노드 번호 값과 오른쪽 노드 번호 값을 계산
            elif arr[i][0] == '-':
                arr[i] = arr[arr[i][1][0]] - arr[arr[i][1][1]]
            elif arr[i][0] == '*':
                arr[i] = arr[arr[i][1][0]] * arr[arr[i][1][1]]
            elif arr[i][0] == '/':
                arr[i] = arr[arr[i][1][0]] // arr[arr[i][1][1]]

    print('#{} {}'.format(t, arr[1]))