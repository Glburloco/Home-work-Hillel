n = int(input("Enter number of files N: "))
files = {}

for _ in range(n):
    file, operations = input("Enter file name and operations (X, R, W): ").split(maxsplit=1)
    files[file] = set(operations.upper().split())

m = int(input("Enter the number of file requests M: "))
requests = []

for _ in range(m):
    operation, file = input("Enter the query (option file name): ").split()
    requests.append((operation.lower(), file))

actions = {
    'write': 'W',
    'read': 'R',
    'execute': 'X'
}

print("Output:")
for operation, file in requests:
    file_operations = files.get(file, set())
    if actions.get(operation) in file_operations:
        print("OK")
    else:
        print("Access denied")