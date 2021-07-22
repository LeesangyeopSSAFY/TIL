# def get_secret_word(words):
#     name = ''
#     for word in words:
#         name += chr(word)
#     return name
# print(get_secret_word([83, 115, 65, 102, 89]))

# def get_secret_number(words):
#     number = 0
#     for word in words:
#         number += ord(word)
#     return number
# print(get_secret_number('tom'))

def get_strong_word(word1, word2):
    sum1 = 0
    sum2 = 0
    for word_1 in word1:
        sum1 += ord(word_1)

    for word_2 in word2:
        sum2 += ord(word_2)
    
    if sum1 > sum2:
        return word1
    else:
        return word2
print(get_strong_word('z', 'a')) 
print(get_strong_word('tom', 'john'))

