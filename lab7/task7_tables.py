# Задание 7. Создать несколько таблиц
import sqlite3

conn = sqlite3.connect("university.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    group_name TEXT)""")

cur.execute("""CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY,
    title TEXT)""")

cur.execute("""CREATE TABLE IF NOT EXISTS marks (
    student_id INTEGER REFERENCES students(id),
    subject_id INTEGER REFERENCES subjects(id),
    mark INTEGER)""")

conn.commit()

cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Таблицы в базе:", [row[0] for row in cur.fetchall()])
conn.close()
