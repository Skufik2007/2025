# Задание 2. Окно с текстовым полем и кнопкой, выводящей текст
import tkinter as tk


def show_text():
    label.config(text="Вы ввели: " + entry.get())


root = tk.Tk()
root.title("Текстовое поле")
root.geometry("300x150")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

button = tk.Button(root, text="Показать", command=show_text)
button.pack()

label = tk.Label(root, text="")
label.pack(pady=10)

root.mainloop()
