# Задание 7. Подсчёт гласных в строке

vowels = "аеёиоуыэюяaeiou"

text = input("Введите строку: ")
count = 0
for letter in text.lower():
    if letter in vowels:
        count += 1

print("Количество гласных:", count)
