n = int(input("Enter number of files N: "))
files = {}

for _ in range(n):
    file, extension = input("Enter file name and operation (X, R, W): ").split(maxsplit=1)
    files[file] = [extension.lower(), extension.upper()]

m = int(input("Enter the number of file requests M: "))
requests = []

for _ in range(m):
    action, file = input("Enter the query (option file name): ").split()
    requests.append((action, file))

actions = {
    'write': 'W',
    'read': 'R',
    'execute': 'X'
}
print("Output:")
for action, file in requests:
    file_extension = files.get(file, '')
    if action == 'write' and 'W' in file_extension:
        print("OK")
    elif action == 'read' and 'R' in file_extension:
        print("OK")
    elif action == 'execute' and 'X' in file_extension:
        print("OK")
    else:
        print("Access denied")