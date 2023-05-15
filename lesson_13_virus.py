n = int(input())
files = {}

for _ in range(n):
    file, extension = input().split(maxsplit=1)
    files[file] = extension.split()

m = int(input())
requests = []

for _ in range(m):
    action, file = input().split()
    requests.append((action, file))

actions = {
    'write': 'W',
    'read': 'R',
    'execute': 'X'
}
print("Output:")
for action, file in requests:
    file_extension = files.get(file, [])
    if actions.get(action) in file_extension or 'R' in file_extension or 'W' in file_extension:
        print("OK")
    else:
        print("Access denied")