# Bloque de Contraseñas

## Introducción

Es común tener cuentas en diferentes sitios web, pero usar la misma contraseña para todos ellos es un mal hábito. Si un sitio sufre una vulnerabilidad de seguridad, los atacantes podrían acceder a todas nuestras cuentas.

Una solución recomendada es usar un gestor de contraseñas que almacene credenciales seguras y complejas. En este ejercicio, crearemos un programa en Python que nos permitirá copiar la contraseña de una cuenta específica al portapapeles, facilitando su uso sin necesidad de memorizarla.

---

## Objetivo del Programa

El programa debe permitir al usuario obtener la contraseña de una cuenta a partir de un diccionario de contraseñas predefinido. Esta contraseña se copiará automáticamente al portapapeles para que el usuario pueda pegarla donde sea necesario.

---

## Pasos para Implementarlo

### 1. Diseño del Programa y Estructuras de Datos

-   El programa se ejecutará desde la línea de comandos.
-   El usuario proporcionará el nombre de la cuenta como argumento.
-   Si la cuenta existe en el diccionario, su contraseña se copiará al portapapeles.
-   Permitir contraseñas seguras sin necesidad de recordarlas manualmente.
-   Se utilizará la biblioteca `pyperclip` para gestionar el portapapeles.

### 2. Manejo de Argumentos en la Línea de Comandos

-   Se utilizará `sys.argv` para capturar los argumentos de la línea de comandos.
-   El primer argumento (`sys.argv[0]`) es el nombre del archivo del programa.
-   El segundo argumento (`sys.argv[1]`) será el nombre de la cuenta cuya contraseña queremos obtener.
-   Si el usuario no proporciona un argumento, se mostrará un mensaje de ayuda explicando cómo usar el programa.

### 3. Copia de la Contraseña al Portapapeles

-   Se almacenarán las contraseñas en un diccionario.
-   Se verificará si la cuenta proporcionada por el usuario existe en el diccionario.
-   Si existe, la contraseña se copiará al portapapeles usando `pyperclip.copy()`.
-   Si la cuenta no existe, se mostrará un mensaje de error indicando que no se encontró la cuenta solicitada.

---

## Uso del Programa

1. Guardar el archivo como `pw.py`.
2. Ejecutar el programa desde la terminal con el siguiente comando:

    ```bash
    python pw.py cuenta_ejemplo
    ```

3. Si la cuenta existe en el diccionario, la contraseña se copiará al portapapeles.
4. El usuario podrá pegarla directamente en el campo correspondiente.

---

## Ejemplo de Uso

```bash
$ python pw.py github
# La contraseña de 'github' ha sido copiada al portapapeles.

$ python pw.py facebook
# Error: No se encontró la cuenta 'facebook'.
```

---

## Consideraciones Finales

-   Se pueden añadir métodos de cifrado para mayor seguridad.
-   Se recomienda integrar con un gestor de contraseñas más robusto.
-   Este programa es una introducción al manejo seguro de credenciales en Python.
