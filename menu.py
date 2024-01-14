import tkinter as tk
from tkinter import Menu

def open_file():
    print("Abrir archivo")

def save_file():
    print("Guardar archivo")

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Menú de Archivo")

menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Abrir", command=open_file)
file_menu.add_command(label="Guardar", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=exit_app)

menu_bar.add_cascade(label="Archivo", menu=file_menu)

root.config(menu=menu_bar)

root.mainloop()
