# Задание 2. Вставить данные в таблицу (сначала запустить task7_tables.py)
import sqlite3

conn = sqlite3.connect("university.db")
cur = conn.cursor()

cur.execute("INSERT INTO students (name, group_name) VALUES (?, ?)",
            ("Филатов Иван", "ИВТ-21"))
cur.executemany("INSERT INTO students (name, group_name) VALUES (?, ?)", [
    ("Петрова Анна", "ИВТ-21"),
    ("Сидоров Олег", "ПИ-22"),
])
cur.executemany("INSERT INTO subjects (title) VALUES (?)", [("Python",), ("Базы данных",)])
cur.executemany("INSERT INTO marks VALUES (?, ?, ?)", [(1, 1, 5), (1, 2, 4), (2, 1, 5)])
conn.commit()

for row in cur.execute("SELECT * FROM students"):
    print(row)
conn.close()
