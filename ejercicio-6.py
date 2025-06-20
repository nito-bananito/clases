# Crear el archivo 'documento.txt' con contenido de ejemplo
with open('documento.txt', 'w', encoding='utf-8') as archivo:
    archivo.write("pepe\n")
    archivo.write("hola\n")
    archivo.write("cafe\n")

print("Archivo 'documento.txt' creado con éxito.")

# Función para reemplazar palabras en un archivo
def reemplazar_palabra(archivo_entrada, archivo_salida, palabra_original, palabra_nueva):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()

        contenido_modificado = contenido.replace(palabra_original, palabra_nueva)

        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido_modificado)

        print(f"Se reemplazó '{palabra_original}' por '{palabra_nueva}' en el archivo '{archivo_salida}'.")

    except FileNotFoundError:
        print(f"El archivo '{archivo_entrada}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Solicitar palabras al usuario
palabra_a_buscar = input("Ingresa la palabra que deseas buscar: ") # Ej: café
palabra_a_reemplazar = input("Ingresa la palabra por la que deseas reemplazarla: ") # Ej: té

# Ejecutar función
reemplazar_palabra('documento.txt', 'modificado.txt', palabra_a_buscar, palabra_a_reemplazar)

