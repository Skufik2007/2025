# Задание 4. Факториал через reduce
from functools import reduce

n = int(input("Введите число: "))
factorial = reduce(lambda x, y: x * y, range(1, n + 1), 1)
print(n, "! =", factorial)
