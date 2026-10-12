# Повышенное задание 6. Создать модуль и импортировать его
import mymath

r = float(input("Введите радиус круга: "))
print("Площадь круга:", round(mymath.circle_area(r), 2))

n = int(input("Введите число: "))
if mymath.is_even(n):
    print("Число чётное")
else:
    print("Число нечётное")
