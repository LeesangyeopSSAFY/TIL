# number = int(input())
# for i in range(1, number + 1):
#     print(i)

# number = int(input())
# for i in range(number, -1, -1):
#     print(i)

# number = int(input())
# total = 0
# for a in range(1, number + 1):
#     total += a
# print("{0}".format(total))

#print('\"파일은 c:\\Windows\\Users\\내문서\\python에 저장이 되었습니다.\"\n나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지.\'')

import math
a, b, c = map(int, input().split(', '))
D = b**2 - 4*a*c
if D > 0:
    D = math.sqrt(D)
    root1 = (-b + D) / 2*a
    root2 = (-b + D) / 2*a
    print("ans1 = {0}, ans2 = {1}".format(root1, root2))
elif D == 0:
    print("single root = {0}".format(-b/2*a))
else:
    print("no root")