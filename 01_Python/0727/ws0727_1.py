def duplicated_letters(words):
    word_list = []
    for word in words:
        word_cnt = words.count(word)
        if word_cnt > 1:
            word_list.append(word)
    return list(set(word_list))
        
print(duplicated_letters('apple'))
print(duplicated_letters('banana'))
