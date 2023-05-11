#1. TypeError - попытка выполнить операцию,
# которая не поддерживается данным типом данных.
# Например:

a = 'hello'
b = 5
c = a + b
# будет вызвана ошибка
# TypeError: can only concatenate str (not "int") to str

#2. NameError - попытка использовать переменную, которая не была определена.
# Например:

print(x)
# будет вызвана ошибка
# NameError: name 'x' is not defined

#3. ZeroDivisionError - попытка выполнить деление на ноль.
# Например:

a = 5
b = 0
c = a / b
# будет вызвана ошибка
# ZeroDivisionError: division by zero

# 4. KeyError - попытка обратиться к несуществующему ключу в словаре.
# Например:

d = {'a': 1, 'b': 2}
print(d['c'])
# будет вызвана ошибка
# KeyError: 'c'

#5. IndentationError - ошибка отступов, когда в коде нарушено правило
# одинакового количества пробелов или табуляций в блоках кода.
# Например:

if a > b:
    print("a is greater than b")
# будет вызвана ошибка
# IndentationError: expected an indented block