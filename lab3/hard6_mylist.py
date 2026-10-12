# Повышенное задание 6. Наследование от встроенного списка с доп. методами


class MyList(list):
    def total(self):
        return sum(self)

    def average(self):
        return sum(self) / len(self)

    def evens(self):
        return MyList([x for x in self if x % 2 == 0])


numbers = MyList([5, 2, 8, 3, 10])
numbers.append(4)  # обычные методы списка тоже работают
print("Список:", numbers)
print("Сумма:", numbers.total())
print("Среднее:", numbers.average())
print("Чётные:", numbers.evens())
