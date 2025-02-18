###
# Lectura de archivos:
# Especifique la ruta del archivo que desea leer.
# Abrir el archivo en modo lectura
###

file_path = "tu directorio/archivo.txt"

with open(file_path, 'r') as file:
    content = file.read()

print(content)
