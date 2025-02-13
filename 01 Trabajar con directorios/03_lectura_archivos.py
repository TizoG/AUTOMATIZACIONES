###
# Lectura de archivos:
# Especifique la ruta del archivo que desea leer.
# Abrir el archivo en modo lectura
###

file_path = "C:/Users/Trabajo/Desktop/Proyectos astro, React y Django/Python/Carpeta ejercicios prueba automatizaciones/Ejercicios/archivo.txt"

with open(file_path, 'r') as file:
    content = file.read()

print(content)
