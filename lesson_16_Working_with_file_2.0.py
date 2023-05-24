# Task_1
import pickle

list_dicts = [
    {'key': 'val1'},
    {'key': 'val2'},
    {'key': 'val3'}
]
with open('data.pickle.txt', 'wb') as file:
    pickle.dump(list_dicts, file)


with open('data.pickle.txt', 'rb') as file:
    list_dicts = pickle.load(file)

for dictionary in list_dicts:
    print(dictionary)

# Task_2
import json

A = {'key': 1, 'key2': True}
B = {'key': 'Hello'}

C = {}
for key, value in A.items():
    if key in B:
        C[key] = [value, B[key]]
    else:
        C[key] = value

for key, value in B.items():
    if key not in C:
        C[key] = value

with open('result.json', 'w') as file:
    json.dump(C, file)


