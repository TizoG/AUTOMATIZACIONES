##
# Tareas que se pueden automatizar con scripts:
#
# Cambie el nombre de varios archivos a la vez.
# Extraer información de un archivo o base de datos.
# Enviar correos electrónicos automáticamente.
# Realice copias de seguridad periódicas de sus datos
##

##
# Creando tu primer script de automatización.
#
# Cambiar el nombre de varios archivos de una carpeta
##

import os

# Especifica la ruta de la carpeta con los archivos.
carpeta = "tu directorio/Carpeta ejercicios prueba automatizaciones"

# Listar todos los archivos en la carpeta
archivos = os.listdir(carpeta)


# Generar el nuevo nombre para el archivo ( en este caso añadimos el _rename)
for archivo in archivos:
    nuevo_nombre = os.path.splitext(
        archivo)[0] + "_rename" + os.path.splitext(archivo)[1]
# Crear la ruta completa del archivo antiguo y del archivo nuevo.
    old_path = os.path.join(carpeta, archivo)
    new_path = os.path.join(carpeta, nuevo_nombre)
# Cambiar el nombre del archivo
    os.rename(old_path, new_path)

print("¡El cambio de nombre se compltó correctamente!")
