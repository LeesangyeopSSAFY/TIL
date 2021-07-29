def dict_invert(my_dict):
    reverse_dict = {}
    for key, val in my_dict.items():
        reverse_dict.setdefault(val, list()).append(key)
    return reverse_dict



print(dict_invert({1: 10, 2: 20, 3: 30}))
print(dict_invert({1: 10, 2: 20, 3: 30, 4: 30}))
print(dict_invert({1: True, 2: True, 3: True}))
