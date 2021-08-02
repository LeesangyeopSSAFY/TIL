# 몫과 나머지 구하기
T = int(input())
test_case = []
cnt = 0

for i in range(T):
    test_case.append(list(map(int,input().split())))

for case in test_case:
    moc = case[0] // case[1] #나눈 몫
    namugi = case[0] % case[1] #나눈 나머지
    cnt += 1
    print(f'#{cnt} {moc} {namugi}')
