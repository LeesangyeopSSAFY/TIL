def reverse_str(list_input):
    # rev_list = [0] * len(list_input)
    for i in range(len(list_input)//2):
        list_input[i], list_input[-i-1] = list_input[-i-1], list_input[i]
    return list_input

S = input()
idx = 0
s = []
ans = ''
while idx < len(S):
    if S[idx] == '<' or '<' in ans:
        if s:
            print(''.join(reverse_str(s)), end='')
            s = []
            ans += '<'
        elif S[idx] != '>':
            ans += S[idx]
        else:
            ans += S[idx]
            print(ans, end='')
            ans = ''
    elif S[idx] == ' ':
        print(''.join(reverse_str(s)), end=' ')
        s = []
    # elif S[idx+1] == '<':
    #     s.append(S[idx])
    #     print(''.join(reverse_str(s)), end='')
    #     s = []
    else:
        s.append(S[idx])
    idx += 1

print(''.join(reverse_str(s)))



    
            
