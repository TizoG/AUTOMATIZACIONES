##
# Eliminar archivos y directorios
##

##
# Para eliminar un archivo
##
import shutil
import os

# Especifique la ruta del archivo a eliminar
file_path = "C:/Users/Trabajo/Desktop/Proyectos astro, React y Django/Python/Carpeta ejercicios prueba automatizaciones/nuevo_nombre.txt"

# Eliminar el archivo
os.remove(file_path)


##
# Para eliminar un directorio y su contenido
# importamos shutil
##

# Especifique la ruta del directorio que se eliminará
directorio_ruta = "C:/Users/Trabajo/Desktop/Proyectos astro, React y Django/Python/Carpeta ejercicios prueba automatizaciones/Ejercicios"

# Eliminar el directorio y su contenido
shutil.rmtree(directorio_ruta)
