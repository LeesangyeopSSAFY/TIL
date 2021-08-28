# 안경이 없어

T = int(input())
for t in range(1, T+1):
    no_hole = ['C', 'E', 'F', 'G', 'H', 'L', 'M', 'N', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    hole = ['A', 'D', 'O', 'P', 'Q', 'R']
    w1, w2 = map(str, input().split())
    ans = 'SAME'
    if len(w1) == len(w2):
        for idx in range(len(w1)):
            if w1[idx] in hole:
                if w2[idx] == 'B' or w2[idx] in no_hole:
                    ans = 'DIFF'
                    break
            elif w1[idx] in no_hole:
                if w2[idx] == 'B' or w2[idx] in hole:
                    ans = 'DIFF'
                    break
            elif w1[idx] == 'B':
                if w2[idx] != 'B':
                    ans = 'DIFF'
                    break
    else:
        ans = 'DIFF'
    print("#{} {}".format(t, ans))