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


emails = re.compile(
    r"""
    [a-zA-Z0-9]+            # Letras o números al inicio
    (?:[.-_][a-zA-Z0-9]+)*    # Puede haber . - _ pero no al inicio o al final
    @
    (?:hotmail|gmail)         # Dominios permitidos
    (?:\.com|\.es|\.net)      # Extensiones permitidas
    """, re.VERBOSE
)
email = emails.findall(
    "aqui puede haber un email pepe@hotmail.com tambien puede haber  juan.perez@gmail.es o ya si eso  user_123-hotmail.net")
print(email)

# TODO: Buscar coincidencias en el texto del portapapeles
# TODO: Copiar resultados al portapapeles y mostrar mensaje
