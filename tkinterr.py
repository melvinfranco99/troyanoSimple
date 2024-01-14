import tkinter as tk

# Crear una ventana
ventana = tk.Tk()

entrada = tk.Label(ventana, text="Introduce: ")
entrada.pack()

# Función para manejar el evento del botón
def obtener_valor():
    valor = entrada.get()
    etiqueta_resultado.config(text="El valor ingresado es: " + valor)

# Crear un campo de entrada
entrada = tk.Entry(ventana)
entrada.pack()

# Crear un botón para obtener el valor ingresado
boton = tk.Button(ventana, text="Obtener valor", command=obtener_valor)
boton.pack()

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
