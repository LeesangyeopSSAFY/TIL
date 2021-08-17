def r_check(lists): # 각 행의 합이 45가 되는지 확인하는 함수
    for c in range(len(lists)):
        total = 0
        for r in range(len(lists)):
            total += lists[r][c]
        if total != 45:
            return False
    return True 

def c_check(lists): # 각 열의 합이 45가 되는지 확인하는 함수
    for r in range(len(lists)):
        total = 0
        for c in range(len(lists)):
            total += lists[r][c]
        if total != 45:
            return False
    return True 

def square(lists): # 각 3*3의 합이 45가 되는지 확인하는 함수
    for r in range(1, 9, 3):
        total = 0
        for c in range(1, 9, 3):
            total += lists[r-1][c-1]
            total += lists[r-1][c]
            total += lists[r-1][c+1]
            total += lists[r][c-1]
            total += lists[r][c]
            total += lists[r][c+1]
            total += lists[r+1][c-1]
            total += lists[r+1][c]
            total += lists[r+1][c+1]
            if total != 45:
                return False
            total = 0
    return True

T = int(input())
for t in range(1, T+1):
    puzzle = []
    for _ in range(9):
        puzzle.append(list(map(int, input().split())))
    
    # 세 함수의 반환값이 모두 True일 경우
    if r_check(puzzle) and c_check(puzzle) and square(puzzle):
        print("#{} 1".format(t))
    else:
        print("#{} 0".format(t))
    