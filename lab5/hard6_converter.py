# Повышенное задание 6. Программа «Конвертер валют»
import tkinter as tk
from tkinter import ttk

# сколько рублей стоит 1 единица валюты
rates = {"RUB": 1, "USD": 92.5, "EUR": 100.2, "CNY": 12.7}


def convert():
    try:
        amount = float(entry.get())
    except ValueError:
        result.config(text="Введите число!")
        return
    rub = amount * rates[from_box.get()]
    value = rub / rates[to_box.get()]
    result.config(text=str(amount) + " " + from_box.get() + " = "
                  + str(round(value, 2)) + " " + to_box.get())


root = tk.Tk()
root.title("Конвертер валют")
root.geometry("300x200")

tk.Label(root, text="Сумма:").pack()
entry = tk.Entry(root)
entry.pack()

from_box = ttk.Combobox(root, values=list(rates), state="readonly")
from_box.set("USD")
from_box.pack(pady=5)

to_box = ttk.Combobox(root, values=list(rates), state="readonly")
to_box.set("RUB")
to_box.pack(pady=5)

tk.Button(root, text="Конвертировать", command=convert).pack()
result = tk.Label(root, text="")
result.pack(pady=10)

root.mainloop()
