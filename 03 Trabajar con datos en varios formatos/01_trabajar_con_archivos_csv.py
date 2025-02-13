##
# Trabajar con archivos CSV
#
# Leer un archivo CSV
"""
Supongamos que tienemos un archivo CSV llamado
'data.csv' con el contenido:
Nombre,Edad;ciudad
Alicia,30 años,Nueva York
Bob,25años,Los Ángeles
Charlie,35 años, Chicago
"""
# Crearemos un archivo CSV
#
# Ruta del directorio
# file_path = "C:/Users/Trabajo/Desktop/Proyectos astro, React y Django/Python/AUTOMATIZACIONES/03 Trabajar con datos en varios formatos/data.csv"
# abrimos en modo escritura
# with open(file_path, 'w') as file:
#   file.write("Nombre,Edad;ciudad\n")
#   file.write("Alicia,30 años,Nueva York\n")
#   file.write("Bob,25 años,Los Ángeles\n")
#   file.write("Charlie,35 años,Chicago\n")
import csv
# Especifique la ruta del archivo CSV
ruta_archivo = "C:/Users/Trabajo/Desktop/Proyectos astro, React y Django/Python/AUTOMATIZACIONES/03 Trabajar con datos en varios formatos/data.csv"

# Abra el archivo CSV para leer
with open(ruta_archivo, 'r') as archivo_csv:
    csv_reader = csv.DictReader(archivo_csv)
    # Iterar sobre las lineas en el arcgivo CSV
    for linea in csv_reader:
        nombre = linea['Nombre']
        edad = linea['Edad']
        ciudad = linea['ciudad']
        # Podemos imprimir los datos o procesarlos
        print(f"{nombre} tiene {edad} años y vive en {ciudad}")
