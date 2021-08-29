# 수 이어가기
def rule(num):
    max_cnt = 0
    for i in range(num+1):
        rule_num = [num, i]
        k = 2
        while rule_num[-1] >= 0:
            result = rule_num[k-2] - rule_num[k-1] # 앞의 앞의 수 뺴기 앞의 수
            rule_num.append(result)
            k += 1
        rule_num.pop() # 위 while문을 돌리면 최초 음수 값이 나올 때까지 출력이 되므로 마지막 값을 제거
        if len(rule_num) > max_cnt:
            max_cnt = len(rule_num)
            ans = rule_num
    return ans

first = int(input())
output = rule(first)
print(len(output))
for j in range(len(output)-1):
    print(output[j], end=' ')
print(output[-1])