n = int(input("Enter you number N: "))
i = 0
while i <= n:
    if i % 3 == 0:
        print(i)
    i += 1

n = int(input("Enter you number N: "))

sum = 0
i = 0
while i <= n:
    if i % 3 == 0:
        sum += i
    i += 1
print("Сумма чисел, какие делятся на 3: ", sum)