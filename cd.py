import tkinter as tk
import subprocess

# Ruta inicial (escritorio)
ruta_actual = "C:\\Users\\Melvin\\Desktop\\"

def ejecutar_comando():
    global ruta_actual
    comando = entrada.get()

    if comando == "pwd":
        # Mostrar la ruta actual en la interfaz
        resultado.config(text=ruta_actual)
    elif comando.startswith("cd "):
        # Comando "cd" para cambiar de directorio
        nueva_ruta = comando[3:]  # Obtener la parte de la ruta después de "cd "
        if nueva_ruta == "..":
            # Retroceder un directorio
            ruta_actual = "\\".join(ruta_actual.split("\\")[:-2]) + "\\"
        else:
            # Cambiar a un nuevo directorio
            ruta_actual = ruta_actual + nueva_ruta + "\\"
    else:
        # Ejecutar el comando en la ruta actual
        subprocess.run(comando, shell=True, cwd=ruta_actual)

# Crear la ventana
ventana = tk.Tk()
ventana.title("Ejecutar Comando")

ventana.geometry("800x600") 

# Crear la entrada de texto
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=10)

# Crear el botón para ejecutar el comando
boton = tk.Button(ventana, text="Ejecutar Comando", command=ejecutar_comando)
boton.pack()

# Crear el widget para mostrar el resultado
resultado = tk.Label(ventana, text="")
resultado.pack()

# Ejecutar la ventana
ventana.mainloop()
