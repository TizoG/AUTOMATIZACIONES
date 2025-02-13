##
# Escribir en un archivo CSV
#

import csv

# Especifique la ruta del archivo CSV de salida
ruta_archivo = "nuevos_datos.csv"

# Datos a escribir

nuevos_datos = [
    {
        'Nombre': 'David',
        'Edad': '28',
        'ciudad': 'San Francisco'
    },
    {
        'Nombre': 'Eva',
        'Edad': '22',
        'ciudad': 'Miami'
    }
]

# Abra el archivo CSV para escribir
with open(ruta_archivo, mode='w', newline="") as archivo_csv:
    campos = ['Nombre', 'Edad', 'ciudad']
    csv_writer = csv.DictWriter(archivo_csv, fieldnames=campos)

    # Escrie el encabezado
    csv_writer.writeheader()

    # Escribe los datos
    for dato in nuevos_datos:
        csv_writer.writerow(dato)

    print("Datos escritos exitosamente en el archivo CSV.")


# Este codigo crea un nuevo archivo CSV llamado nuevos_datos.csv
# y escibe en él los datos específicados.
##
