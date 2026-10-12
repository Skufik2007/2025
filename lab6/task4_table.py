# Задание 4. Страница с таблицей данных
from flask import Flask, render_template

app = Flask(__name__)

students = [
    {"name": "Иванов Иван", "group": "ИВТ-21", "mark": 5},
    {"name": "Петрова Анна", "group": "ИВТ-21", "mark": 4},
    {"name": "Сидоров Олег", "group": "ПИ-22", "mark": 3},
]


@app.route("/")
def table():
    return render_template("table.html", students=students)


if __name__ == "__main__":
    app.run(debug=True)
