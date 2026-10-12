# Задание 7. Окно с меню (File → Exit)
import tkinter as tk
from tkinter import messagebox


def about():
    messagebox.showinfo("О программе", "Лабораторная работа 5")


root = tk.Tk()
root.title("Окно с меню")
root.geometry("300x200")

menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="About", command=about)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

root.config(menu=menubar)
root.mainloop()
