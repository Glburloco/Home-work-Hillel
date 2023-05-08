#task_1
numbers = []
for i in range (5):
    num = int(input('Enter you number: '))
    numbers.append(num)
print(numbers)

#task_2
A = [1, 2, 3, 4, 5]
A.pop()
print(A)

#task_3
A = []
for i in range (10):
    num = int(input('Enter you number: '))
    A.append(num)

N = int(input('Enter you number N: '))

count = 0
for num in A:
    if num == N:
        count += 1
print(f'The list A has the number {N} repeated {count} times')

#task_4
N = int(input("Enter number of numbers: "))
A = []
for i in range(N):
    num = int(input("Enter you number N: "))
    A.append(num)

A.reverse()
print(A)

#task_5
A = []
for i in range(5):
    num = int(input("Enter you number: "))
    A.append(num)

C = []
for num in A:
    if num > 5:
        C.append(num)

print(C)

#task_6
N = int(input("Enter number of numbers: "))
A = []
for i in range(N):
    num = int(input("Enter you number: "))
    A.append(num)

min_num = A[0]
max_num = A[0]
for num in A:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

print(f"Min number in list: {min_num}")
print(f"Max number in list: {max_num}")

#task_7
text = input("Enter you text: ")
count = 0
for char in text:
    if char.isdigit():
        count += 1

print(f"The text has number: {count}")
