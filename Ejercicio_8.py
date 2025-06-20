# Programa para filtrar líneas que contienen una palabra específica

# Solicita al usuario la palabra que quiere buscar
palabra_buscada = input("Introduce la palabra que deseas buscar: ")

# Abre el archivo original para leer y el nuevo archivo para escribir
with open("libro.txt", "r", encoding="utf-8") as archivo_entrada, open("filtrado.txt", "w", encoding="utf-8") as archivo_salida:
    for linea in archivo_entrada:
        # Verifica si la palabra buscada está en la línea (ignorando mayúsculas/minúsculas)
        if palabra_buscada.lower() in linea.lower():
            archivo_salida.write(linea)

print("Filtrado completado. Revisa el archivo 'filtrado.txt'.")
