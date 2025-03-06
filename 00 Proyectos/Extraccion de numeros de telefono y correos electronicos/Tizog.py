import regex as re
import pyperclip

# Recuperamos el texto copiado en la variable texto
texto = pyperclip.paste()

# asignamos a la variable la expresion regular que nos buscara los números de telefonos
numeros_telefono = re.compile(
    r"""
    \+?\d{1,4}[\s-]?                # Código de país, opcional (+34, 001, etc.)
    \(?\d{1,4}\)?[\s-]?             # Código de área (puede tener paréntesis, 1 a 4 dígitos)
    \d{1,3}                         # Primer grupo de 1 a 3 dígitos
    [\s-]?                           # Separador opcional (espacio o guion)
    \d{3}                            # Segundo grupo de 3 dígitos
    [\s-]?                           # Separador opcional (espacio o guion)
    \d{3,4}                          # Últimos 3 o 4 dígitos
    """, re.VERBOSE)  # Modo verbose para facilitar la lectura

# en esta variable asignamos el findall para que busque todos los números de telefono.
telefonos = numeros_telefono.findall(
    texto)

# formateamos para verlo mejor
print("*"*20)
print()
print("Los números de telefonos encontrados son: ")
print()

# Iniciamos un bucle for para que nos lo de cada uno en una linea diferente y no en una lista
for numero in telefonos:
    print(numero)


print()
print("*"*20)


# creamos la variable que le asignamos la expresión regular para que ahora nos encuentre emails. Aquí solo queremos los emails con extensiones (hotmail o gmail) y las(.com,.es,.net)
emails = re.compile(
    r"""
    [a-zA-Z0-9]+            # Letras o números al inicio
    (?:[.-_][a-zA-Z0-9]+)*    # Puede haber . - _ pero no al inicio o al final
    @
    (?:hotmail|gmail)         # Dominios permitidos
    (?:\.com|\.es|\.net)      # Extensiones permitidas
    """, re.VERBOSE
)

# variable para buscar todos los correos
email = emails.findall(
    texto)

print()
print("Los emails encontrados son: ")
print()

# bucle for para que nos de los correo en una linea diferente
for e in email:
    print(e)


print(e)
print()


# TODO: Meter todo esto en una sola función
# TODO: averiguar si es mejor una funcion que llame a las otras funciones o meterlo todo en una sola
