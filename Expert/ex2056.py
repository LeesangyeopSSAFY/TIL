t = int(input())
Date_lists = []
cnt = 0
m_31 = ['01', '03', '05', '07', '08', '10', '12'] # 31일인 달
m_30 = ['04', '06', '09', '11'] # 30일인 달

for i in range(t):
    Date_lists += [input()] #리스트 속에 리스트 대신 문자열이 들어가도록 입력을 받기
    #Date_lists.append(list(map(str,input().split())))


for data in Date_lists:
    cnt += 1
    if data[4:6] in m_31 and int(data[6:8]) in range(32) and len(data) == 8:   #data값의 월 자리의 문자열이 31인 달에 포함이고 일 자리의 문자열의 정수형이 31에 포함이면
        print(f'#{cnt} {data[:4]}/{data[4:6]}/{data[6:8]}')
    elif data[4:6] in m_30 and int(data[6:8]) in range(31) and len(data) == 8:  #data값의 월 자리의 문자열이 30인 달에 포함이고 일 자리의 문자열의 정수형이 30에 포함이면
        print(f'#{cnt} {data[:4]}/{data[4:6]}/{data[6:8]}')
    elif data[4:6] == '02' and int(data[6:8]) in range(29) and len(data) == 8:   #2월일 경우
        print(f'#{cnt} {data[:4]}/{data[4:6]}/{data[6:8]}')
    else:                                                   #날짜가 유효하지 않을 경우
        print(f'#{cnt} -1')


