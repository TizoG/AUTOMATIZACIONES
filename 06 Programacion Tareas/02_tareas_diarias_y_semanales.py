##
# Programacion de tareas diarias y semanales
#
# Tarea para que se ejecute todos los dias a las 10:00
# Programar la tarea diariamente a las 10:00
import schedule
import time


def tarea():
    tiempo_actual = time.strftime("%H:%M:%S")
    print(f"La tarea se ejecuto a las {tiempo_actual}")


schedule.every().day.at("10:00").do(tarea)

##
# Para programar una tarea semanalmente,
# Todos los martes a las 3:30 pm

schedule.every().tuesday.at("15:30").do(tarea)
