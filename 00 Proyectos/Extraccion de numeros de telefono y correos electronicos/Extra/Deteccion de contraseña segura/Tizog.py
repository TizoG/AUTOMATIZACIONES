import regex as re

text = "asutsasaAWWWsdasdw"  # contrasena no segura
text1 = "asut3SAoUF"  # contrasena  segura
pattern = r"[\w]{8,}[\d]+"
match = re.search(pattern, text)


if match:
    print("Contraseña segura")
else:
    print("Contraseña no segura")
