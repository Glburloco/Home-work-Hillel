def cache_decorator(func):
    cache_dict = {}

    def wrapper(*args, **kwargs):
        if func.__name__ not in cache_dict:
            cache_dict[func.__name__] = {}

        key = (args, tuple(sorted(kwargs.items())))

        if func.__name__ not in cache_dict:
            cache_dict[func.__name__] = {}
        if key in cache_dict[func.__name__]:
            return cache_dict[func.__name__][key]
        else:
            result = func(*args, **kwargs)
            cache_dict[func.__name__][key] = result
        return result

    return wrapper


@cache_decorator
def triangle_area(a: float, b: float) -> float:
    print(f'Вызвана функция triangle_area с аргументами {a} и {b}')
    return a * b


@cache_decorator
def circle_area(r: float) -> float:
    print(f'Вызвана функция circle_area с аргументом {r}')
    return 3.14 * (r * r)


print('Результат выполнения triangle_area(5, 10):', triangle_area(5, 10))  # Тело функции выполниться так как функция
# вызывается в первый раз с такими аргументами
print('Результат выполнения triangle_area(5, 10):', triangle_area(5, 10))  # Тело функции не выполниться так как функция
# ранее вызывалась с такими аргументами
print('Результат выполнения circle_area(20):', circle_area(20))  # Тело функции выполниться так как функция вызывается в
# первый раз с такими аргументами
print('Результат выполнения triangle_area(10, 10):', triangle_area(10, 10))  # Тело функции выполниться так как функция
# вызывается в первый раз с такими аргументами
print('Результат выполнения circle_area(20):', circle_area(20))  # Тело функции не выполниться так как функция ранее
# вызывалась с такими аргументами
