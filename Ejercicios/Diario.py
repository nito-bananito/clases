# Paso 1: Importar el módulo datetime
from datetime import datetime
ahora = datetime.now()
print("Justo ahora es:",ahora)

# Paso 2: Solicitar al usuario que ingrese el texto para su entrada del diario
entrada = input("Escribe algo en el diario: ")

# Paso 3: Abrir el archivo diario.txt en modo de adición ('a')
with open("diario.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"{ahora}\n{entrada}\n\n")

# Paso 6: Mostrar un mensaje de confirmación
print("Tu texto ha sido guardado en 'diario.txt'")