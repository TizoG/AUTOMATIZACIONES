##
# Cambiar el nombre y mover archivos
# Para cambiar el nombre o mover un archivo usamos el modulo shutil
##
import shutil

##
# Especifique la ruta del archivo original y el nuevo nombre o ruta
##

ruta_original = "C:/Users/Trabajo/Desktop/Proyectos astro, React y Django/Python/Carpeta ejercicios prueba automatizaciones/Ejercicios/archivo.txt"
nueva_ruta = "C:/Users/Trabajo/Desktop/Proyectos astro, React y Django/Python/Carpeta ejercicios prueba automatizaciones/nuevo_nombre.txt"

##
# Cambiar el nombre o mover el archivo
#
# Esto cambiara el nombre o movera el archivo especificado
##
shutil.move(ruta_original, nueva_ruta)
