# Повышенное задание 6. Работа с PostgreSQL через psycopg2
# Перед запуском: установить PostgreSQL, создать базу lab7, pip install psycopg2-binary
import psycopg2

conn = psycopg2.connect(dbname="lab7", user="postgres", password="postgres",
                        host="localhost", port=5432)
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price NUMERIC(10, 2))""")

cur.execute("INSERT INTO products (name, price) VALUES (%s, %s)", ("Ноутбук", 85000))
cur.execute("INSERT INTO products (name, price) VALUES (%s, %s)", ("Мышь", 1200))
conn.commit()

cur.execute("UPDATE products SET price = %s WHERE name = %s", (80000, "Ноутбук"))
conn.commit()

cur.execute("SELECT id, name, price FROM products")
for row in cur.fetchall():
    print(row)

cur.close()
conn.close()
