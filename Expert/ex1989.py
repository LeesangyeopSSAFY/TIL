T = int(input())
str_list = []
for t in range(T):
    str_list.append(input())

for case in str_list:
    result = True
    for i in range(int(len(case)/2)):
        for j in range(len(case)//2):
            if case[j] != case[-j-1]:
                result = result and False
            else:
                result = result and True

    print(result)
    