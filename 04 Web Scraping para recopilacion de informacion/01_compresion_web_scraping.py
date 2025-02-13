##
# Web Scraping
#
# Para el Web Scraping usaremos 2 blibliotecas de Python
# BeautifulSoup y Requests
#
# Instalación de bibliotecas
# pip install beautifulsoup4 requests
#
# Recopilacion de informacion de na pagina web

"""
Supongamos que deseamos recopilar titulares de noticias de última hora
de un sitio web de noticias. Aquí un ejemplo:
"""

import requests
from bs4 import BeautifulSoup

# URL de la web de la que desea recopilar información

URL = "https://www.elconfidencial.com/"

# Enviar una solicitud GET a la web
respuesta = requests.get(URL)

# Comprobar si la solicitud fue exitosa
if respuesta.status_code == 200:
    # Analizamos el contenido HTML de la web con BeautifoulSoup
    soup = BeautifulSoup(respuesta.text, 'html.parser')

    # Encuentra los elementos que contienen los títulos de las noticias
    titulos_noticias = soup.find_all('h3', class_='ac-principal__title')

    # Iterar a través de los elementos e imprimir los titulos
    for titulo in titulos_noticias:
        print(titulo.text)
else:
    print("Error al acceder a la página web.")


"""
Este código envia una solicitud GET a la página web especificada, analiza el contenido 
HTML de la web con BeautifulSoup y extrae los titulares de las noticiaspara imprimirlos.
"""
##
# Aquí podemos modificarlo como queramos podemos quitarle la class_
# Podemos iterar con un id si son muchos titulos
# Podemos quitar espacios por delante y por detras
# ...
"""
titulos_noticias = soup.find_all('h3', class_='ac-principal__title')

    # Iterar a través de los elementos e imprimir los titulos
    for titulo in titulos_noticias:
        print(titulo.text)
"""
