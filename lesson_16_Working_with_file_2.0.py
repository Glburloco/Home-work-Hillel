import json
def mge_dicts(a, b):
    c = a.copy()
    for key, value in b.items():
        if key in c:
            if isinstance(c[key], list):
                c[key].append(value)
            else:
                c[key] = [c[key], value]
        else:
            c[key] = value
    return c

A = {'key': 1, 'key2': True}
B = {'key': 'Hello'}

C = mge_dicts(A, B)

with open('result.json', 'w') as file:
    json.dump(C, file)

print("Значення словника A:", A)
print("Значення словника B:", B)
print("Значення словника C:", C)
