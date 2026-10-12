# Задание 2. Сумма всех нечётных чисел до N


def sum_odd(n):
    s = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            s += i
    return s


n = int(input("Введите N: "))
print("Сумма нечётных чисел до", n, "=", sum_odd(n))
