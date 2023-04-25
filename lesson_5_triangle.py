n = int(input("Enter you side of a triangle: "))

if n >= 1:
    print("triangle #1:")
    for i in range(n, 0, -1):
        print("*" * i)

    print("triangle #2:")
    for i in range(1, n+1):
        print("*" * i)

    print("triangle #3:")
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * i)

    print("triangle #4:")
    for i in range(1, n+1):
        print(" " * (n - i) + "*" * i)