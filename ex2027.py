# 대각선 출력하기
texts = ['+', '+', '+', '+', '+']
for i in range(5): #5번 실행
    for j in range(5): #texts의 문자열 번호
        if i == j:
            texts[i] = '#' #실행한 숫자와 문자열 번호가 같은 경우 그 값을 #으로 변환        
    print(''.join(texts)) 
    texts = ['+', '+', '+', '+', '+'] #texts 리스트 초기화