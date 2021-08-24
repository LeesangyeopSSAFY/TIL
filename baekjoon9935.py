string = input()
bomb = input()
stack = []
for i in range(len(string)):
    if string[i] != bomb[-1]: # 문자열을 순회하면서 i 인덱스의 문자가 폭탄 문자열의 마지막 문자와 다르다면
        stack.append(string[i]) # 스택에 문자 추가
    elif string[i] == bomb[-1]: # 인덱스의 문자가 폭탄 문자열의 마지막 문자와 같으면
        stack.append(string[i]) # 일단 스택에 문자 추가 후
        if ''.join(stack[-len(bomb):]) == bomb: # 스택에 폭탄 문자열 길이만큼 쌓인 단어가 폭탄 문자열이라면
            for _ in range(len(bomb)): # 폭탄 문자열의 길이만큼 pop
                stack.pop() 
        
if stack:
    print(''.join(stack))
else:
    print('FRULA')


