# ⭐ Agregar Viñetas Automáticamente al Marcado Wiki ⭐

## 📝 Descripción

Este script de Python facilita la edición de listas en Wikipedia, agregando automáticamente viñetas (`* `) al inicio de cada línea de un texto copiado al portapapeles.

📅 **Caso de uso:**
Si tienes una lista grande y necesitas agregar viñetas manualmente, este script automatiza la tarea en segundos.

---

## ⚙️ Cómo Funciona

1. Copias una lista de elementos al portapapeles.
2. Ejecutas el script en Python.
3. El script procesa el texto y agrega `* ` al inicio de cada línea.
4. El nuevo texto con viñetas se copia automáticamente al portapapeles.
5. Pegas la lista formateada donde la necesites.

---

## 📚 Ejemplo de Uso

### ✅ Texto original copiado:

```
Lista de animales
Listas de vida en el acuario
Listas de biologia por abreviatura de autor
Listas de cultivares
```

### 🔄 Texto transformado:

```
* Lista de animales
* Listas de vida en el acuario
* Listas de biologia por abreviatura de autor
* Listas de cultivares
```

---

## 🛠️ Instalación y Ejecución

### ♻️ Requisitos:

-   Python 3.x
-   Biblioteca `pyperclip` (para manejar el portapapeles)

### 💻 Instalación de dependencias:

Ejecuta el siguiente comando para instalar `pyperclip` si no lo tienes:

```bash
pip install pyperclip
```

### 💪 Ejecutar el script:

Guarda el siguiente código en un archivo `viñetas.py` y ejecútalo:

```python
import pyperclip

# Obtener el texto del portapapeles
texto = pyperclip.paste().strip()
lineas = texto.split("\n")

# Agregar '* ' al inicio de cada línea
lineas = ["* " + linea for linea in lineas if linea.strip()]

# Unir las líneas y copiar el resultado al portapapeles
texto = "\n".join(lineas)
pyperclip.copy(texto)

print("✅ Texto formateado copiado al portapapeles.")
```

### 📚 Uso:

1. Copia una lista de texto al portapapeles.
2. Ejecuta el script en la terminal con:
    ```bash
    python viñetas.py
    ```
3. Pega el texto formateado donde lo necesites.

---

## 🌟 Beneficios

-   ⏳ **Ahorro de tiempo**: Evita escribir asteriscos manualmente.
-   ⚖️ **Consistencia**: Todas las líneas siguen el formato correctamente.
-   🔧 **Simplicidad**: Un script pequeño pero poderoso.

---

## 🚀 Contribuir

Si tienes mejoras o sugerencias, no dudes en compartirlas. ✨

---

## 🌟 Autor

Creado con ❤️ para facilitar la edición en Wikipedia.
