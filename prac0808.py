# a = {'사과', '바나나', '수박'}
# a.update({'토마토', '복숭아'}, {'뚜알기'})
# print(a)

class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1

    def __del__(self):
        Doggy.num_of_dogs -= 1

    def bark(self):
        print('멍멍!')

    @classmethod
    def get_status(cls):
        print(f'Birth: {cls.birth_of_dogs}, Currnet: {cls.num_of_dogs}')

d1 = Doggy('초코', '푸들')
d2 = Doggy('앙꼬', '웰시코기')
d3 = Doggy('복실이', '진돗개')

d1.bark()
d2.bark()
d3.bark()
Doggy.get_status()