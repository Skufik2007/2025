# Задание 4. Обновить запись
import sqlite3

conn = sqlite3.connect("university.db")
cur = conn.cursor()

student_id = int(input("ID студента: "))
new_group = input("Новая группа: ")

cur.execute("UPDATE students SET group_name = ? WHERE id = ?", (new_group, student_id))
conn.commit()

if cur.rowcount == 0:
    print("Студент не найден")
else:
    print("Запись обновлена:")
    print(cur.execute("SELECT * FROM students WHERE id = ?", (student_id,)).fetchone())
conn.close()
