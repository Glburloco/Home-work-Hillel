import math
a = int(input("первая сторона:"))
b = int(input("вторая сторона:"))
c = int(input("третья сторона:"))
p = (a + b + c)/2
s = p * (p - a) * (p - b) * (p - c)
print(math.sqrt(s))