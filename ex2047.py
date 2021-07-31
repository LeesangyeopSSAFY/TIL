def make_up(words):
    new_words = ''
    for word in words:
        if word.isalpha() and word.islower(): # 단어가 문자이면서 소문자일 경우
            new_words += word.upper() # 문자를 대문자로 변경 후 추가
        # 그 외의 경우 그냥 문자 그대로 추가
        else: 
            new_words += word
    return new_words

print(make_up('The_headline_is_the_text_indicating_the_nature_of_the_article_below_it.'))