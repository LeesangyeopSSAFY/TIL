import random

class ClassHelper:
    def __init__(self, lists):
        self.lists = lists

    def pick(self, n):
        return random.sample(self.lists, n)

    def match_pair(self):
        new_list = []
        random_list = random.sample(self.lists, len(self.lists))
        if len(random_list) % 2 == 0:
            for i in range(0, len(random_list), 2):
                new_list.append([random_list[i], random_list[i+1]])
            return new_list
        elif len(random_list) % 2:
            for j in range(0, len(random_list)-3, 2):
                new_list.append([random_list[j], random_list[j+1]])
            new_list.append(random_list[-3:])
            return new_list

ch = ClassHelper(['김이나', '이지은', '조세호', '박재정', '정인'])
print(ch.match_pair())