##
# Escribir en un archivo JSON

import json

# Datos a escribir
nuevos_datos = {
    "nombre": "Eva",
    "edad": 22,
    "ciudad": "Miami"
}

# Especifique la ruta del archivo JSON de salida
ruta_archivo = "new_data.json"

# Abra el archivo JSON para escribir
with open(ruta_archivo, mode='w') as json_file:
    json.dump(nuevos_datos, json_file)

    print("Datos escritos exitosamente en el archivo JSON")

# Este código crea un nuevo archivo JSON y escribe los
# datos especificados en él
##
