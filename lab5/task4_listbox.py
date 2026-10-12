# Задание 4. Список (Listbox) и выбор элемента
import tkinter as tk


def on_select(event):
    index = listbox.curselection()
    if index:
        label.config(text="Вы выбрали: " + listbox.get(index[0]))


root = tk.Tk()
root.title("Listbox")
root.geometry("250x250")

listbox = tk.Listbox(root)
for item in ["Python", "Java", "C++", "JavaScript", "Go"]:
    listbox.insert(tk.END, item)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", on_select)

label = tk.Label(root, text="Ничего не выбрано")
label.pack()

root.mainloop()
