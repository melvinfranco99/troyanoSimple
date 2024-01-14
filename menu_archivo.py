import tkinter as tk
from tkinter import Menu, filedialog

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".pyw", filetypes=[("Python", "*.pyw")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write("import tkinter as tk\n\nroot = tk.Tk()\nroot.title('Mi Aplicación')\nlabel = tk.Label(root, text='Hola, mundo!')\nlabel.pack(pady=10, padx=10)\nroot.mainloop()")
        print("Guardado como:", file_path)

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Menú de Archivo")

menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Guardar como .py", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=exit_app)

menu_bar.add_cascade(label="Archivo", menu=file_menu)

root.config(menu=menu_bar)

root.mainloop()
