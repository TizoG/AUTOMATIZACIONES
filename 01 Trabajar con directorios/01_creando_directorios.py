"""
Para crear un directorio para almacenar archivos
Podemos hacerlo importando el modulo "os"
"""
import os

# Especifica la ruta del nuevo directorio.
new_directory_path = "C:/Users/Trabajo/Desktop/Proyectos astro, React y Django/Python/Carpeta ejercicios prueba automatizaciones/Ejercicios"

# Crear el directorio
# os.mkdir(new_directory_path)


# Listado de archivos en un directorio
# Especificar la ruta del directorio
directorio = "C:/Users/Trabajo/Desktop/Proyectos astro, React y Django/Python/Carpeta ejercicios prueba automatizaciones"

# Listar todos los archivos en el directorio
archivos = os.listdir(directorio)
for archivo in archivos:
    print(archivo)  # Imprime todos los nombres de los archivos del directorio
