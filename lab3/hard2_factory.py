# Повышенное задание 2. Паттерн Factory (фабрика)


class Dog:
    def speak(self):
        return "Гав!"


class Cat:
    def speak(self):
        return "Мяу!"


class Cow:
    def speak(self):
        return "Муу!"


class AnimalFactory:
    # фабрика создаёт объект по названию
    @staticmethod
    def create(kind):
        if kind == "собака":
            return Dog()
        elif kind == "кошка":
            return Cat()
        elif kind == "корова":
            return Cow()
        else:
            raise ValueError("Неизвестное животное")


kind = input("Кого создать (собака, кошка, корова)? ")
animal = AnimalFactory.create(kind)
print(kind, "говорит:", animal.speak())
