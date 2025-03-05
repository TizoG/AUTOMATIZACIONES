import regex as re
import pyperclip

# Recuperamos el texto copiado en la variable texto
texto = pyperclip.paste()

numeros_telefono = re.compile(
    r"""
    \+?\d{1,4}[\s-]?              # Código de país, opcional (+34, 001, etc.)
    \(?\d{1,4}\)?[\s-]?           # Código de área (puede tener paréntesis)
    \d{3}                         # 3 dígitos
    [\s-]?                         # Separador opcional (espacio o guion)
    \d{3}                         # 3 dígitos
    [\s-]?                         # Separador opcional (espacio o guion)
    \d{3,4}                       # Últimos 3 o 4 dígitos
    """, re.VERBOSE)  # Modo verbose para facilitar la lectura
telefonos = numeros_telefono.findall(
    texto)

print(telefonos)


# TODO: Crear expresion regular para extraer correos electronicos
# TODO: Buscar coincidencias en el texto del portapapeles
# TODO: Copiar resultados al portapapeles y mostrar mensaje
