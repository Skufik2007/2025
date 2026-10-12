# Задание 7. Декоратор для логирования вызова функции


def log(func):
    def wrapper(*args):
        print("Вызов функции", func.__name__, "с аргументами", args)
        result = func(*args)
        print("Функция", func.__name__, "вернула", result)
        return result
    return wrapper


@log
def add(a, b):
    return a + b


@log
def square(x):
    return x * x


add(2, 3)
square(5)
