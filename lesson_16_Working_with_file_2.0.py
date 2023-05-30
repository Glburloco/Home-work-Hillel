import json
from collections import defaultdict
def merge_dicts(a, b):
    c = defaultdict(list)
    for key, value in a.items():
        c[key].append(value)
    for key, value in b.items():
        c[key].append(value)
    return dict(c)
def save_dict_to_file(d, filename):
    with open(filename, 'w') as file:
        json.dump(d, file)

A = {'key': 1, 'key2': True}
B = {'key': 'Hello'}

C = merge_dicts(A, B)

save_dict_to_file(C, 'result.json')

print("Значення словника A:", A)
print("Значення словника B:", B)
print("Значення словника C:", C)
