# 직사각형을 만드는 방법
N = int(input())
square = 0
# i를 1부터 N까지로 설정하면 시간이 오래 걸려서 런타임 에러가 난다
for i in range(1, int(N**0.5) + 1):
    for j in range(i, N+1): # i번째부터 시작하는 j를 통해 i길이의 정사각형이 만들어지는 후부터
        if i * j <= N:      # 이전에 나오지 않았던 새로운 직사각형을 만들 수 있다
            square += 1
        else:
            break

print(square)