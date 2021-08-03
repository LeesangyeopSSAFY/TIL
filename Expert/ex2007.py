T = int(input())
t_words = []
cnt = 0
for t in range(T): # T번 만큼 입력 받음
    t_words.append(input())

for words in t_words:
    cnt += 1
    for i in range(1, len(words)//2):
        if words[0:i] == words[i+1:i+1+i]:
            print(f'#{cnt} {len(words[0:i])+1}')
            break
        else:
            continue
