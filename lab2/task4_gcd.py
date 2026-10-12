# Задание 4. НОД двух чисел (перебором делителей)


def gcd(a, b):
    for d in range(min(a, b), 0, -1):
        if a % d == 0 and b % d == 0:
            return d


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print("НОД чисел", a, "и", b, "равен", gcd(a, b))
