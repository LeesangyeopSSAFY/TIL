str_input = input()
str_cnt = [0] * 26 # 각 문자별로 문자의 개수 체크
for i in str_input:
    str_cnt[ord(i)-65] += 1

holsu_cnt = 0 # 홀수의 개수가 1을 넘으면 회문이 되지 않으므로 홀수의 개수를 카운트
holsu_alpha = ''
alpha = ''
for j in range(len(str_cnt)):
    if str_cnt[j] % 2: # 문자가 나온 횟수가 홀수일 경우
        holsu_cnt += 1
        holsu_alpha += chr(j+65)
    alpha += chr(j+65) * (str_cnt[j]//2) # alpha에 나온 횟수에서 2로 나눈 몫만큼 문자로 반환해서 더한다.
ans = alpha + holsu_alpha + alpha[::-1] # alpha + 홀수 개수인 문자 + alpha를 뒤집은 문자

if holsu_cnt > 1: # 홀수의 개수가 1이 넘을 경우
    print("I'm Sorry Hansoo")
else:
    print(ans)

