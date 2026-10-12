# Повышенное задание 2. Мемоизация функции через декоратор
import time


def memoize(func):
    cache = {}

    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper


def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


@memoize
def fib_memo(n):
    if n < 2:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)


start = time.time()
print("fib(30) =", fib(30), "без кэша:", round(time.time() - start, 3), "сек")

start = time.time()
print("fib(30) =", fib_memo(30), "с кэшем:", round(time.time() - start, 5), "сек")
