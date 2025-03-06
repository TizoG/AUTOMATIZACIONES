import re


cadena = "   Hola mundo    "
pattern = r"^\s+|\s+$"
result = re.sub(pattern, "", cadena)
print(result)


cadena = "xxHola mundoxxx"
caracter = "x"
caracter_escapado = re.escape(caracter)
pattern = f"^[{caracter_escapado}]+|[{caracter_escapado}]+$"
result = re.sub(pattern, "", cadena)
print(result)
