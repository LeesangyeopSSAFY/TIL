def reverse_str(list_input): # 문자열 뒤집기를 위한 reverse_str함수 정의
    for i in range(len(list_input)//2):
        list_input[i], list_input[-i-1] = list_input[-i-1], list_input[i]
    return list_input

S = input()
idx = 0
s = [] # 문자 뒤집기용 단어 리스트
ans = '' # 태그 사이의 문자 출력용
while idx < len(S):
    if S[idx] == '<' or '<' in ans: #태그가 시작되거나 태그 속의 단어일 경우
        if s: # 태그가 생기기 전에 뒤집을 문자가 있다면
            print(''.join(reverse_str(s)), end='') # 문자 뒤집고 바로 연속되게 다음 문자가 출력되도록
            s = [] # 다시 뒤집을 문자 리스트 초기회
            ans += '<' # ans에 태그 시작 '<' 추가
        elif S[idx] != '>': # idx값이 닫는 태그가 나올 때까지 ans에 문자 추가
            ans += S[idx]
        else: # 닫는 문자가 나온다면 ans를 출력하고 ans를 다시 초기화
            ans += S[idx]
            print(ans, end='')
            ans = ''
    elif S[idx] == ' ': # idx 값이 공백이 나올 경우
        print(''.join(reverse_str(s)), end=' ') # 문자를 뒤집어서 출력 후 s 리스트를 다시 초기회
        s = []
    else: # 태그 사이에 있는 문자도 아니고 공백이 아닐 경우
        s.append(S[idx]) # 문자 뒤집기용 리스트에 값을 추가
    idx += 1

print(''.join(reverse_str(s))) # 마지막 문자열은 공백이 나오지 않으니 뒤집을 문자가 있다면 마지막 문자열이 뒤집어서 출력된다.



    
            
