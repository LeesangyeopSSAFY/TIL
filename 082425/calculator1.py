T = 11
for t in range(1, T+1):
    len_tc = int(input())
    tc = input()
    operator = {
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1,
        '(': 0
    }
    stack = []
    postfix_notation = []
    for token in tc:
        if token.isnumeric(): # token이 숫자라면
            postfix_notation += token
        elif token == '(': # (은 들어갈 때 가장 우선순위가 높으므로 그냥 stack에 push
            stack.append(token)
        elif token == ')': # )가 나오면 (가 나올 때까지 모두 pop
            while stack[-1] != '(':
                postfix_notation += stack.pop()
            stack.pop() # (까지 pop
        elif stack and operator[token] <= operator[stack[-1]]: # token보다 낮은 연산자를 만날 때까지 pop후 postfix_notation에 push
            while stack and operator[token] <= operator[stack[-1]]:
                postfix_notation += stack.pop()
            stack.append(token) # token을 stack에 push
        else: # stack이 비어있거나, stack의 마지막 연산자가 token보다 우선 순위가 높다면 push
            stack.append(token)
    while stack: # 수식이 끝났고 스택이 빌 때까지 모두 pop
        postfix_notation += stack.pop()

    for i in postfix_notation: # 후위 표기법으로 표시한 것을 순회하면서
        if i.isnumeric(): # 숫자라면 stack에 push
            stack.append(i)
        else: # 연산자라면 연산
            r = int(stack.pop())
            l = int(stack.pop())
            if i == '+':
                stack.append(l + r)
            elif i == '-':
                stack.append(l - r)
            elif i == '*':
                stack.append(l * r)
            elif i == '/':
                stack.append(l // r)

    print("#{} {}".format(t, stack.pop()))