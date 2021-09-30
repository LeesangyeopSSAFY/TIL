T = int(input())

hex_to_bin = {
    '0':'0000', '1':'0001', '2':'0010', '3':'0011',
    '4':'0100', '5':'0101', '6':'0110', '7':'0111',
    '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
    'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'
}

pattern_dict = {
    "211": 0,
    "221": 1,
    "122": 2,
    "411": 3,
    "132": 4,
    "231": 5,
    "114": 6,
    "312": 7,
    "213": 8,
    "112": 9,
}

for tc in range(1, T + 1):
    # N: 배열의 세로 크기
    # M: 배열의 가로 크기
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]

    # 열 중복 제거
    data_set = list(set(data))
    N2 = len(data_set)

    data_to_binary = [""] * N2
    for i in range(N2):
        for j in range(M):
            data_to_binary[i] += hex_to_bin[data_set[i][j]]

    # 0으로만 이루어진 행 제거
    clean_data_to_binary = []
    for x in data_to_binary:
        if int(x) != 0:
            clean_data_to_binary.append(x)

    result = 0
    visited = []
    for binary_code in clean_data_to_binary:
        decode = []
        # 암호 비율
        a = b = c = d = 0
        binary_code = binary_code.rstrip("0")
        L = len(binary_code)
        for i in range(L - 1, -1, -1):
            if c == 0 and binary_code[i] == "1":
                d += 1
            # d > 0 조건이 없으면, a 자리에서 읽어야 할 "0"을 자기가 읽어버린다.
            elif d > 0 and b == 0 and binary_code[i] == "0":
                c += 1
            elif a == 0 and binary_code[i] == "1":
                b += 1
            elif b > 0 and c > 0 and d > 0 and binary_code[i] == "0":
                # 뒤에 3자리만 고려하여도 구분이 가능함
                # 비율 고려
                div = min(b, c, d)
                b //= div
                c //= div
                d //= div
                key = str(b) + str(c) + str(d)
                decode = [pattern_dict[key]] + decode
                a = b = c = d = 0

            if len(decode) == 8:
                if ((decode[0] + decode[2] + decode[4] + decode[6]) * 3 + decode[1] + decode[3] + decode[5] + decode[7]) % 10 == 0:
                    if decode not in visited:
                        result += sum(decode)
                        visited.append(decode)
                decode = []
    print(f"#{tc} {result}")