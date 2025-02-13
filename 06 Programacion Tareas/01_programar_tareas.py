##
# Programar Tareas
#
# El modulo schedule permite ejecutar funciones en momentos específicos
#
# Instalación del módulo
#
# Programación de tareas sencilla

import schedule
import time

# Función a ejecutar


def tarea():
    tiempo_actual = time.strftime("%H:%M:%S")
    print(f"La tarea se ejecutó a las {tiempo_actual}")

# Programar la tarea cada minuto
schedule.every(1).minutes.do(tarea)


print("Iniciando el bucle principal...")
# Ejecución continua del programa
while True:
    print("Ejecutando run_pending()...")
    schedule.run_pending()
    time.sleep(1)
