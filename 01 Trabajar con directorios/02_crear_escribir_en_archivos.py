# Trabajar con archivos

# Crear y escribir en archivos
# Para crear un nuevo archivo y escribir en el,
# puede utilizar el siguiente codigo:
###
import os

# Especifique la ruta del archivo que desea crear.
file_path = "C:/Users/Trabajo/Desktop/Proyectos astro, React y Django/Python/Carpeta ejercicios prueba automatizaciones/Ejercicios/archivo.txt"


# abrimos el archivo en modo escritura
with open(file_path, "w") as file:
    file.write("Hola, este es un archivo de ejemplo.\n")
    file.write("¡Python es fantastico para la automatizacion!\n")
