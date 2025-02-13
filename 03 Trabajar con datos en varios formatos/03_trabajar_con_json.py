##
# Trabajar con JSON
#
# Lectura de un archivo JSON
# suponiendo que tengamos un archivo JSON llamado data.json
# puede leer y procesar estos datos
import json

# especifique la ruta del archivo JSON
ruta_archivo = "C:/Users/Trabajo/Desktop/Proyectos astro, React y Django/Python/AUTOMATIZACIONES/03 Trabajar con datos en varios formatos/data.json"

# Abra el archivo JSON para leer
with open(ruta_archivo, mode='r') as json_file:
    datos = json.load(json_file)

    nombre = datos['nombre']
    edad = datos['edad']
    ciudad = datos['ciudad']

    # Haz lo que quieras con los datos, como imprimirlos o procesarlos
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")
