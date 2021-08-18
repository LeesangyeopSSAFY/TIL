T = int(input())
cnt = 0
for t in range(T):
    cnt += 1
    N = int(input())
    trow = [1]
    y = [0]
    for n in range(N):
        print(trow)
        trow=[left+right for left,right in zip(trow+y, y+trow)] # 구글링
    n += 1

######################################################
# 위에 코드로 설명을 제대로 못 할 것 같아서 다시 풀었습니다...
T = int(input())
for t in range(1, T+1):
    N = int(input())

    pascal = []
    # 각 1의 값을 가진 N 크기의 파스칼 삼각형 생성
    for n in range(1, N+1):
        pascal.append([1]*n)

    # 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성되므로 1부터 마지막 줄 전까지
    for i in range(1, N-1):
        for j in range(len(pascal[i])-1):
            pascal[i+1][j+1] = pascal[i][j] + pascal[i][j+1]

    print("#{}".format(t))
    for ans in pascal:
        print(' '.join(map(str, ans))) # ans는 숫자를 포함한 리스트이므로

    