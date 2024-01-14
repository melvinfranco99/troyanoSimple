import tkinter as tk
from tkinter import Menu, filedialog
import subprocess

ruta_actual = "C:\\Users\\Melvin\\Desktop\\"

def virus():
    global ruta_actual
    subprocess.run('mkdir nuevaCarpeta1', shell=True, cwd=ruta_actual)




def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".pyw", filetypes=[("Python", "*.py")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write("import tkinter as tk\n\nventana = tk.Tk()\nventana.title('Mi Aplicación')\nlabel = tk.Label(ventana, text='Hola, mundo!')\nlabel.pack(pady=10, padx=10)\nventana.mainloop()")
        print("Guardado como:", file_path)

def exit_app():
    ventana.destroy()

ventana = tk.Tk()
ventana.title("Inversión")

ventana.geometry("800x600") 

menu_bar = Menu(ventana)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Guardar como .py", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=exit_app)

menu_bar.add_cascade(label="Archivo", menu=file_menu)
menu_bar.add_cascade(label="Opciones")
menu_bar.add_cascade(label="Ayuda")

ventana.config(menu=menu_bar)

RENTABILIDAD = (0.1/12)

#espacios enter
enter = tk.Label(ventana, text='\n')
enter.pack()

rent = tk.Label(ventana, text='Teniendo en cuenta que la rentabilidad es del 10%% anual...')
rent.pack()

#espacios enter
enter = tk.Label(ventana, text='\n')
enter.pack()

# Entrada Inversion
inversion_mensual_label = tk.Label(ventana, text='Introduce inversion mensual: ')
inversion_mensual_label.pack()

entrada_inversion = tk.Entry(ventana)
entrada_inversion.pack()

# Entrada Meses
numero_meses_label = tk.Label(ventana, text='Introduce numero meses: ')
numero_meses_label.pack()

entrada_meses = tk.Entry(ventana)
entrada_meses.pack()


def calculo():
    inversion_mensual = float(entrada_inversion.get())
    numero_meses = int(entrada_meses.get())
    ganancia_bruta = 0

    for i in range(numero_meses):
        ganancia_neta = (ganancia_bruta + inversion_mensual) * RENTABILIDAD
        ganancia_bruta = ganancia_neta + (ganancia_bruta + inversion_mensual)

    sacarGanancia.config(text="\nLas ganancias son de: {:.2f} euros".format(ganancia_bruta))
    virus()


#espacios enter
enter = tk.Label(ventana, text='\n')
enter.pack()
# Crear un botón para obtener el valor ingresado
boton = tk.Button(ventana, text="Obtener ganancias", command=calculo)
boton.pack()

sacarGanancia = tk.Label(ventana, text="")
sacarGanancia.pack()

ventana.mainloop()
