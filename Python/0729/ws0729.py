class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle(Point):
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def get_area(self):
        result = abs(self.point1.x - self.point2.x) * abs(self.point1.y - self.point2.y)
        return result

    def get_perimeter(self):
        result = (abs(self.point1.x - self.point2.x) + abs(self.point1.y - self.point2.y)) * 2
        return result

    def is_square(self):
        if abs(self.point1.x - self.point2.x) == abs(self.point1.y - self.point2.y):
            return True
        else:
            return False


p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())
p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())