# N = int(input())
# switch = list(map(int, input().split()))
# stu_num = int(input())
# for _ in range(stu_num):
#     stu_inp = input()
#     if stu_inp[0] == '1': #남학생이라면
#         for i in range(int(stu_inp[2])-1, len(switch), int(stu_inp[2])):
#             if switch[i] == 0:
#                 switch[i] = 1
#             else:
#                 switch[i] = 0
#             # switch[i] = (switch[i] + 1) % 2
#     elif stu_inp[0] == '2': #여학생이라면
#         j = int(stu_inp[2]) - 1
#         switch[j] = (switch[j] + 1) % 2
#         k = 1
#         while 0 <= j-k and j+k < N and switch[j-k] == switch[j+k]:
#             switch[j-k] = (switch[j-k] + 1) % 2
#             switch[j+k] = (switch[j+k] + 1) % 2
#             k += 1
#
# for i in range(len(switch)):
#     print(switch[i], end=' ')
#     if  i != 0 and i % 20 == 0:
#         print()

def change(num):
    switch[num] = (switch[num]+1) % 2
    return
    # if switch[num] == 0:
    #     switch[num] = 1
    # else:
    #     switch[num] = 0
    # return

N = int(input())
switch = [-1] + list(map(int, input().split()))
students = int(input())
for _ in range(students):
    stu, num = map(int, input().split())
    if stu == 1:
        for i in range(num, N + 1, num):
            change(i)
    else:
        change(num)
        for k in range(N // 2):
            if num + k > N or num - k < 1: break
            if switch[num + k] == switch[num - k]:
                change(num + k)
                change(num - k)
            else:
                break

for i in range(1, N + 1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()