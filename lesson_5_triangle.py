n = int(input("Enter you side of a triangle: "))

if n >= 2:
    print("triangle #1:")
    i = 1
    while i <= n:
        print("*" * i)
        i += 1

    print("triangle #2:")
    i = n
    while i >= 1:
        print("*" * i)
        i -= 1

    print("triangle #3:")
    i = 1
    while i <= n:
        print(" " * (n - i) + "*" * i)
        i += 1

    print("triangle #4:")
    i = n
    while i >= 1:
        print(" " * (n - i) + "*" *i)
        i -= 1