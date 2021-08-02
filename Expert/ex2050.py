inp_str = input()  
num_str = ''
for spell in inp_str:
    num_str = str(ord(spell) - 64) # 각 문자를 ord()함수를 통해 아스키코드로
    print(num_str, end=' ') # end = ' '를 통해 빈칸 생성