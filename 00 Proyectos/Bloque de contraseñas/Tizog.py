import pyperclip
import random
import string
contraseñas = {

}


def pw():
    """
    Obtiene la contraseña de una cuenta y la copia al portapapeles.

    Si la cuenta existe en el diccionario, se copia la contraseña al portapapeles.
    Si no existe, se crea una nueva contraseña y se guarda en el diccionario.

    :param nombre_cuenta: El nombre de la cuenta
    :type nombre_cuenta: str
    """

    nombre_cuenta = input("Introduc el nombre de la cuenta: ")
    password_cuenta = random.choices(
        string.ascii_letters + string.digits + string.punctuation, k=16)
    if nombre_cuenta in contraseñas:
        pyperclip.copy("".join(contraseñas[nombre_cuenta]))
        print(
            f"La contraseña  de la cuenta {nombre_cuenta} se ha copiado al portapapeles.")

    else:
        contraseñas[nombre_cuenta] = password_cuenta
        pyperclip.copy("".join(contraseñas[nombre_cuenta]))
        print(
            f"La contraseña de la cuenta {nombre_cuenta} se ha copiado al portapapeles.")

    print("".join(contraseñas[nombre_cuenta]))


while True:
    opcion = input("Deseas copiar una contraseña? (s/n):")
    if opcion == "n":
        break
    else:
        pw()
