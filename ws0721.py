# values = [1, 2, 3, 4, 5]
# def list_sum():
#     total = 0
#     for value in values:
#         total += value
#     return total
# print(list_sum())

dicts = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]
def dict_list_sum():
    total = 0
    for value in dicts:
        total += value['age']
    return total
print(dict_list_sum())

# values = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]
# def all_list_sum():
#     total = 0
#     for value in values:
#         for i in value:
#             total += i
#     return total
# print(all_list_sum())