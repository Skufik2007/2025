# Задание 2. Класс «Студент» с методом вывода информации


class Student:
    def __init__(self, name, group, course):
        self.name = name
        self.group = group
        self.course = course

    def show_info(self):
        print("Студент:", self.name)
        print("Группа:", self.group)
        print("Курс:", self.course)


student = Student("Филатов Иван", "ИВТ-21", 2)
student.show_info()
