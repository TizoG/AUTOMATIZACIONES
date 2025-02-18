##
# Realizar solucitudes GET
#
# Solicitud get para obtener datos de una API meteorologica

import requests

# URL de la API de AEMET
URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "Aqui tu api key"
params = {
    "q": "Granada",
    "appid": API_KEY,
    "units": "metric"
}

respuesta = requests.get(URL, params=params)

if respuesta.status_code == 200:
    datos = respuesta.json()
    print("La temperatura en Granada es de:", datos["main"]["temp"], "ºC")
    print("La sensación termica en Granada es de:",
          datos["main"]["feels_like"], "ºC")
    print("La temperatura minima en Granada es de:",
          datos["main"]["temp_min"], "ºC")
    print("La temperatura maxima en Granada es de:",
          datos["main"]["temp_max"], "ºC")
    print("La humedad en Granada es de:", datos["main"]["humidity"], "%")
    print("La presión en Granada es de:", datos["main"]["pressure"], "hPa")
else:
    print("De esa ciudad no tengo datos.")
