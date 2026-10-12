# Задание 2. Отфильтровать чётные числа из списка

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x: x % 2 == 0, numbers))

print("Список:", numbers)
print("Чётные:", even)
