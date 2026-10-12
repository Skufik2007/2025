# Повышенное задание 2. Рисование фигур мышью
import tkinter as tk

start_x = 0
start_y = 0


def press(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y


def release(event):
    shape = shape_var.get()
    if shape == "Линия":
        canvas.create_line(start_x, start_y, event.x, event.y, width=2)
    elif shape == "Прямоугольник":
        canvas.create_rectangle(start_x, start_y, event.x, event.y, outline="blue", width=2)
    elif shape == "Овал":
        canvas.create_oval(start_x, start_y, event.x, event.y, outline="red", width=2)


def clear():
    canvas.delete("all")


root = tk.Tk()
root.title("Рисование мышью")

shape_var = tk.StringVar(value="Прямоугольник")
panel = tk.Frame(root)
panel.pack()
for name in ["Линия", "Прямоугольник", "Овал"]:
    tk.Radiobutton(panel, text=name, variable=shape_var, value=name).pack(side=tk.LEFT)
tk.Button(panel, text="Очистить", command=clear).pack(side=tk.LEFT)

canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()
canvas.bind("<ButtonPress-1>", press)
canvas.bind("<ButtonRelease-1>", release)

root.mainloop()
