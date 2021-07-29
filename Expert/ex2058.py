N = input() #문자열로 입력받음
sum_N = 0
#반복문을 통해 각 자리수를 정수형으로 변환 후 sum
for n in N: 
    sum_N += int(n)
print(sum_N)