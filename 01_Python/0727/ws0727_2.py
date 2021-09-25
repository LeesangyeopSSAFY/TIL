def low_and_up(words):
    new_word = ''
    for i in range(len(words)):
        if i % 2: # 홀수 자리의 경우 words의 자리를 대문자로 변경 후 new_word에 추가
            new_word += words[i].upper()
        else: # 짝수 자리의 경우 소문자로 변경 후 new_word에 추가
            new_word += words[i].lower()
    return new_word


print(low_and_up('apple'))
print(low_and_up('banana'))