import pyperclip

# Obtenemos el texto del portapapeles
texto = pyperclip.paste()
# Separamos el texto en lineas individuales
lineas = texto.split("\n")

# mediante el bucle for recorremos todas las lineas y agregamos el * al principio de cada linea
for linea in range(len(lineas)):
    lineas[linea] = "* " + lineas[linea]

# Une las lineas modificdas en un solo texto
texto = "\n".join(lineas)
pyperclip.copy(texto)
print("✅ Texto formateado copiado al portapapeles.")
print(texto)
