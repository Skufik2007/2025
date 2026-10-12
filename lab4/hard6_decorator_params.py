# Повышенное задание 6. Декоратор с параметрами


def repeat(times):
    def decorator(func):
        def wrapper(*args):
            for i in range(times):
                func(*args)
        return wrapper
    return decorator


@repeat(3)
def hello(name):
    print("Привет,", name)


hello("Иван")
