# num1 = 0.1*3
# num2 = 0.3
# import math
# print(math.isclose(num1, num2))

# print('"파일은 c:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다."\n나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지\'')

# temp =36.5
# print('입실 불가') if temp >= 37.5 else print('입실 가능')

# def fibo_recursion(a):
#     if a < 2:
#         return a
#     else:
#         return fibo_recursion(a-1) + fibo_recursion(a-2)

# print(fibo_recursion(5))

class Circle:
    pi = 3.14
    x = 0
    y = 0
    z = 0

    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y

    def area(self):
        return self.pi * self.r * self.r

    def circumstance(self):
        return 2 * self.pi * self.r

    def center(self):
        return (self.x, self.y)

circle = Circle(3, 2, 4)
print(f'{circle.area():.2f}')
print(circle.circumstance())