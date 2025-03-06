# 📞📧 Extractor de Números de Teléfonos y Direcciones de Correo Electrónico

## 📌 Descripción

¿Alguna vez te has encontrado con la aburrida tarea de buscar números de teléfono y direcciones de correo electrónico dentro de un documento extenso o una página web? Hacerlo manualmente puede ser tedioso y propenso a errores.

Este proyecto busca automatizar este proceso al extraer automáticamente la información relevante del texto copiado en tu portapapeles. Solo necesitas copiar el texto de interés y ejecutar el programa, que se encargará de:

✅ Extraer todos los números de teléfono y direcciones de correo electrónico.
✅ Formatearlos en un solo bloque de texto.
✅ Pegarlos en el portapapeles para su fácil uso.

---

## 🏗️ Planificación del Proyecto

Antes de comenzar con el código, es importante definir un esquema claro de lo que debe hacer el programa:

1️⃣ Obtener el texto del portapapeles.
2️⃣ Buscar todos los números de teléfono y direcciones de correo electrónico.
3️⃣ Formatear los resultados en una salida clara y concisa.
4️⃣ Copiar los resultados nuevamente al portapapeles.
5️⃣ Mostrar un mensaje si no se encuentran coincidencias.

Con esta hoja de ruta clara, podemos centrarnos en cada paso de forma independiente, asegurando que el código sea manejable y comprensible.

---

## 🛠️ Funcionalidad del Código

El código implementará las siguientes características:

🔹 Uso del módulo `pyperclip` para copiar y pegar cadenas de texto.
🔹 Creación de expresiones regulares para encontrar coincidencias de:

-   Números de teléfono.
-   Direcciones de correo electrónico.
    🔹 Búsqueda de todas las coincidencias en el texto, no solo la primera.
    🔹 Formateo adecuado de los resultados.
    🔹 Mensaje de notificación si no se encuentra ninguna coincidencia.

---

## 🏃‍♂️ Ejemplo de Uso

1️⃣ Copia el texto que contiene números de teléfono y correos electrónicos.
2️⃣ Ejecuta el programa.
3️⃣ Los resultados extraídos se copiarán automáticamente en el portapapeles.
4️⃣ Pega los resultados donde los necesites.

📌 **Ejemplo de texto de prueba:**
[No Starch Press Contact Page](http://www.nostarch.com/contactus.htm)

---
