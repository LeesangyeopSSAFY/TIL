T = int(input())
t_words = []
cnt = 0
list1 = [1, 2, 3, 5, 6, 10]
for t in range(T): # T번 만큼 입력 받음
    t_words.append(input())

for words in t_words:
    cnt += 1
    for i in range(1, 11):
        if i in list1 and words[0:i] == words[-i:] and words[0:i] == words[i:2*i]:
            print(f'#{cnt} {i}')
            break
        elif i in [4, 7] and words[0:i] == words[-i-2:-2] and words[0:i] == words[i:2*i]:
            print(f'#{cnt} {i}')
            break
        elif i == 8 and words[0:i] == words[-i-6:-6] and words[0:i] == words[i:2*i]:
            print(f'#{cnt} {i}')
            break
        elif i == 9 and words[0:i] == words[-i-3:-3] and words[0:i] == words[i:2*i]:
            print(f'#{cnt} {i}')
            break
