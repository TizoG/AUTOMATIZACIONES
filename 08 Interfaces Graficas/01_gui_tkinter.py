##
# Creando una GUI simple con Tkinter

import tkinter as tk
import os

# Función para acción de automatización


def realizar_automatizacion():
    directorio = "C:/Users/Trabajo/Desktop/Proyectos astro, React y Django/Python/Carpeta ejercicios prueba automatizaciones"
    archivos = os.listdir(directorio)
    result_label.config(text="\n".join(archivos))


# crear ventana principal
ventana = tk.Tk()
ventana.title("Mi automatización")

# Crear boton
button = tk.Button(ventana, text="Ejecutar automatización",
                   command=realizar_automatizacion)

button.pack()

# Crear etiqueta para mostar el resultado
result_label = tk.Label(ventana, text="", justify="left")
result_label.pack()

# Iniciar la interfaz gráfica
ventana.mainloop()
