# 1대 1 가위바위보
rcp = list(map(int, input().split()))

if rcp[0] == 1 and rcp[1] == 2:
    print('B')
elif rcp[0] == 1 and rcp[1] == 3:
    print('A')
elif rcp[0] == 2 and rcp[1] == 1:
    print('A')
elif rcp[0] == 2 and rcp[1] == 3:
    print('B')
elif rcp[0] == 3 and rcp[1] == 1:
    print('B')
elif rcp[0] == 3 and rcp[1] == 2:
    print('A')
else:
    print('Error')